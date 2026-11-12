"""Offline packaging contracts; live skill loading is evidenced separately."""

import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "working-style", "development-architecture", "microservice-testing",
    "planning-tool-preferences", "coding-style",
}
MANIFEST = ROOT / ".github/plugin/plugin.json"


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def assert_local_links(test, source):
    """Reject missing resources, path escapes and missing Markdown anchors."""
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
        if "://" in link:
            continue
        path, _, anchor = link.partition("#")
        target = (source.parent / path).resolve()
        test.assertTrue(target.is_relative_to(ROOT), f"Escaping link: {link}")
        test.assertTrue(target.is_file(), f"Missing link: {link}")
        if anchor:
            headings = re.findall(r"^#+ (.+)$", target.read_text(encoding="utf-8"), re.M)
            anchors = {re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-") for h in headings}
            test.assertIn(anchor, anchors, f"Missing anchor: {link}")


class PluginContractTests(unittest.TestCase):
    def test_legacy_manifest_has_only_supported_selected_fields(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(
            set(manifest),
            {"name", "version", "description", "author", "repository", "license", "skills"},
        )
        self.assertEqual(manifest["name"], "agentic-persona")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(manifest["skills"], ["skills/"])
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(manifest["repository"], "https://github.com/hoffe86/agentic-tools")

    def test_only_one_manifest_and_no_marketplace_or_injection_components(self):
        excluded = {".git", ".worktrees", "__pycache__", ".probe"}
        names = {
            p.relative_to(ROOT).as_posix()
            for p in ROOT.rglob("*")
            if p.is_file() and not (set(p.relative_to(ROOT).parts) & excluded)
        }
        self.assertEqual({p for p in names if p.endswith("plugin.json")}, {".github/plugin/plugin.json"})
        self.assertFalse(any("marketplace.json" in p for p in names))
        self.assertFalse(any(
            set(Path(p).parts) & {"hooks", "agents", "commands", "com.github.copilot"}
            or Path(p).name in {".mcp.json", "mcp.json", "hooks.json", "lsp.json"}
            for p in names
        ))

    def test_exactly_the_five_selected_skills_and_required_resources(self):
        self.assertEqual(
            {p.relative_to(ROOT / "skills").as_posix()
             for p in (ROOT / "skills").rglob("*") if p.is_file()},
            {
                "working-style/SKILL.md",
                "development-architecture/SKILL.md",
                "development-architecture/references/platform-preferences.md",
                "microservice-testing/SKILL.md",
                "planning-tool-preferences/SKILL.md",
                "planning-tool-preferences/references/ado.md",
                "coding-style/SKILL.md",
                "coding-style/references/csharp.md",
                "coding-style/references/python.md",
                "coding-style/references/typescript.md",
                "coding-style/references/clean-code-developer.md",
            },
        )
        self.assertFalse(any(p.is_symlink() for p in (ROOT / "skills").rglob("*")))

    def test_skill_frontmatter_names_and_discovery_descriptions(self):
        for name in sorted(SKILLS):
            with self.subTest(skill=name):
                text = read(f"skills/{name}/SKILL.md")
                frontmatter = text.split("---\n", 2)[1]
                # The package uses only a plain name and a folded YAML scalar.
                self.assertRegex(
                    frontmatter,
                    r"\Aname: [a-z0-9-]+\ndescription: >-\n(?:  \S[^\n]*\n)+\Z",
                )
                self.assertIn(f"name: {name}\n", frontmatter)
                self.assertIn("description: >-\n", frontmatter)
                self.assertNotIn("allowed-tools:", frontmatter)
                self.assertGreater(len(text.split("---\n", 2)[2].split()), 200)

    def test_all_relative_documentation_and_skill_links_resolve(self):
        paths = [ROOT / "README.md"]
        paths += list((ROOT / "docs").rglob("*.md"))
        paths += list((ROOT / "skills").rglob("*.md"))
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                assert_local_links(self, path)

    def test_license_is_unchanged_from_original_repository(self):
        provenance = json.loads(read("docs/provenance.json"))
        self.assertEqual(
            hashlib.sha256((ROOT / "LICENSE").read_bytes()).hexdigest(),
            "72ca7f17fb91de38183f115e295e08fa539f507107b65b4a61fb67495746e6f5",
        )
        self.assertEqual(provenance["license"]["sha256"],
                         hashlib.sha256((ROOT / "LICENSE").read_bytes()).hexdigest())

    def test_provenance_covers_only_selected_source_ownership(self):
        provenance = json.loads(read("docs/provenance.json"))
        imported = set(provenance["source_inventory"])
        authored = set(provenance["authored_skills"])
        self.assertEqual(imported | authored, SKILLS)
        self.assertTrue(imported.isdisjoint(authored))
        self.assertEqual(provenance["source_inventory"], {
            "working-style": ["SKILL.md"],
            "development-architecture": ["SKILL.md"],
            "microservice-testing": ["Microservice-Test-Concept.md"],
        })
        self.assertEqual(
            {item["source"] for item in provenance["sources"]},
            {
                "~/.copilot/skills/working-style/SKILL.md",
                "~/.copilot/skills/development-architecture/SKILL.md",
                "~/Eigene/Concepts/Test Concept/Microservice-Test-Concept.md",
            },
        )
        for item in provenance["sources"]:
            with self.subTest(source=item["source"]):
                self.assertRegex(item["sha256"], r"^[a-f0-9]{64}$")
                self.assertEqual(set(item), {"source", "sha256"})
        self.assertEqual(
            {item["source"]: item["sha256"] for item in provenance["sources"]},
            {
                "~/.copilot/skills/working-style/SKILL.md":
                    "c3e9324f3a3aaa0e2e5820a62c8d8fc5e76c84f5c6dd82d975b78414f3a9c8c4",
                "~/.copilot/skills/development-architecture/SKILL.md":
                    "0ee9b44e3477e841c21a192a3508b4cc63a6f175e6a0f1b73902a9e6dfca120e",
                "~/Eigene/Concepts/Test Concept/Microservice-Test-Concept.md":
                    "feabd17305cb7ebd34e0df3fed7ac783e54d9f8a4c618eb816404e648c119aee",
            },
        )
        self.assertIn("owner-authorized", read("docs/provenance.md"))

    def test_authored_planning_skill_provenance_and_reference_inventory(self):
        authored = json.loads(read("docs/provenance.json"))["authored_skills"]
        self.assertIn("planning-tool-preferences", authored)
        skill = authored["planning-tool-preferences"]
        root = ROOT / "skills/planning-tool-preferences"
        self.assertEqual(set(skill["resources"]), {
            "SKILL.md", "references/ado.md",
        })
        self.assertEqual(
            {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()},
            set(skill["resources"]),
        )
        reference = (ROOT / skill["research_reference"]).resolve()
        self.assertEqual(reference, root / "references/ado.md")
        self.assertTrue(reference.is_file())
        self.assertRegex(
            read("skills/planning-tool-preferences/SKILL.md"),
            r"\[[^\]]+\]\(references/ado\.md\)",
        )
        self.assertNotIn("sha256", skill)
        inspiration = skill["historical_inspiration"]
        self.assertEqual(inspiration["license"], "MIT")
        self.assertEqual(
            inspiration["url"],
            "https://github.com/hoffe86/agile-agents/blob/"
            "dd4710004eb257db39f781515dcfb2c07f58bdb6/"
            "plugins/agile-agents-ado/skills/ado-work-items/SKILL.md",
        )
        self.assertEqual(inspiration["notice"], "Copyright (c) 2026 hoffe86")

    def test_authored_coding_skill_provenance_and_reference_inventory(self):
        authored = json.loads(read("docs/provenance.json"))["authored_skills"]
        skill = authored["coding-style"]
        root = ROOT / "skills/coding-style"
        references = {
            "references/csharp.md", "references/python.md",
            "references/typescript.md",
            "references/clean-code-developer.md",
        }
        self.assertEqual(set(skill), {"resources", "basis", "research_references"})
        self.assertTrue(skill["basis"].strip())
        self.assertCountEqual(skill["resources"], {"SKILL.md"} | references)
        self.assertEqual(
            {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()},
            set(skill["resources"]),
        )
        self.assertCountEqual(
            skill["research_references"],
            {f"skills/coding-style/{path}" for path in references},
        )
        entry = root / "SKILL.md"
        self.assertCountEqual(
            re.findall(r"\[[^\]]+\]\((references/[^)]+)\)",
                       entry.read_text(encoding="utf-8")),
            references,
        )
        for path in [entry, *(root / name for name in sorted(references))]:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.is_file())
                assert_local_links(self, path)

    def test_research_reference_is_the_self_contained_skill(self):
        provenance = json.loads(read("docs/provenance.json"))
        target = (ROOT / provenance["research_reference"]).resolve()
        self.assertTrue(target.is_relative_to(ROOT / "skills/microservice-testing"))
        self.assertEqual(target, ROOT / "skills/microservice-testing/SKILL.md")
        self.assertTrue(target.is_file())

    def test_native_instructions_are_separate_compact_opt_in(self):
        text = read("native/copilot-instructions.md")
        self.assertLess(len(text.split()), 180)
        self.assertIn("native skill tool", text)
        self.assertIn("do not install anything implicitly", text)
        self.assertFalse((ROOT / "copilot-instructions.md").exists())
        self.assertFalse((ROOT / ".github/copilot-instructions.md").exists())
        self.assertNotIn("native/", read(".github/plugin/plugin.json"))
        self.assertIn("does not activate", read("README.md"))

    def test_personal_consent_cannot_waive_solution_or_harness_controls(self):
        working = read("skills/working-style/SKILL.md")
        architecture = read("skills/development-architecture/SKILL.md")
        native = read("native/copilot-instructions.md")
        self.assertIn("do not commit or push without explicit user", working)
        self.assertIn("cannot waive harness safety", working)
        self.assertIn("subordinate to\nsolution technical constraints", architecture)
        self.assertIn("may tighten consent, never waive controls", architecture)
        self.assertIn("stricter consent, never waive", native)

    def test_agent_answers_use_ste_principles_without_claiming_conformance(self):
        text = " ".join(read("skills/working-style/SKILL.md").split())
        for rule in (
            "For agent answers", "ASD-STE100 Simplified Technical English principles",
            "short sentences with one point", "active voice and direct verbs",
            "consistent, unambiguous terminology", "avoid idioms and filler",
            "Preserve exact code/API identifiers and technical meaning",
            "Honour the requested language", "not certified or full conformance",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)

    def test_platform_preferences_are_scoped_not_an_unrelated_stack_default(self):
        architecture = read("skills/development-architecture/SKILL.md")
        platform = read("skills/development-architecture/references/platform-preferences.md")
        self.assertIn("no blanket .NET, Azure or microservices default", architecture)
        self.assertIn("only for the\nmatching technologies already selected", architecture)
        self.assertIn("Apply **only matching sections**", platform)
        self.assertIn("not a general deployment recipe", architecture)

    def test_guidance_has_no_migration_log_or_personal_absolute_setup_path(self):
        for path in list((ROOT / "skills").rglob("*.md")) + [ROOT / "README.md"]:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("/Users/", text)
                self.assertNotIn("/home/hoffe", text)
                if path.name == "SKILL.md":
                    self.assertNotIn("2026-11-08", text)
                    self.assertNotIn("c3e9324f", text)
                    self.assertNotIn("## Changelog", text)

    def test_product_docs_describe_current_package_not_run_history(self):
        self.assertFalse((ROOT / "docs/runtime-evidence.json").exists())
        self.assertFalse((ROOT / "docs/source-map.md").exists())
        for path in [ROOT / "README.md", *list((ROOT / "docs").glob("*.md"))]:
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("agentic-tools@0.1.0", text)
                self.assertNotIn("task5-", text)
                self.assertNotIn("transcript", text.lower())
        self.assertIn("agentic-persona", read("docs/compatibility.md"))

    def test_text_artifacts_have_no_trailing_whitespace_and_end_with_newline(self):
        paths = [ROOT / "README.md", MANIFEST]
        paths += list((ROOT / "docs").glob("*"))
        paths += list((ROOT / "skills").rglob("*.md"))
        paths += list((ROOT / "skills").rglob("*.json"))
        paths += list((ROOT / "native").glob("*.md"))
        paths += list((ROOT / "tests").glob("*.py"))
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n"))
                self.assertNotIn("\r", text)
                self.assertTrue(all(line == line.rstrip() for line in text.splitlines()))


if __name__ == "__main__":
    unittest.main()
