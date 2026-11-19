import unittest
import yaml
import os


class TestGpqaDiamondCotZeroshotConfig(unittest.TestCase):
    """Validate gpqa_diamond_cot_zeroshot task configuration."""

    def setUp(self):
        config_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "lm_eval",
            "tasks",
            "gpqa",
            "cot_zeroshot",
            "gpqa_diamond_cot_zeroshot.yaml",
        )
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    def test_dataset_name(self):
        self.assertEqual(self.config["dataset_name"], "gpqa_diamond")

    def test_task_name(self):
        self.assertEqual(self.config["task"], "gpqa_diamond_cot_zeroshot")

    def test_doc_to_text_present(self):
        self.assertIn("doc_to_text", self.config)
        self.assertIn("The best answer is (X)", self.config["doc_to_text"])

    def test_includes_base(self):
        self.assertEqual(self.config["include"], "_gpqa_cot_zeroshot_yaml")


if __name__ == "__main__":
    unittest.main()
