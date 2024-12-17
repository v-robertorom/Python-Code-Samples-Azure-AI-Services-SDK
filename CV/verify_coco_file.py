from cognitive_service_vision_model_customization_python_samples import check_coco_annotation_file, AnnotationKind, Purpose
import pathlib
import json

# Assuming your COCO file is named "annotations.json" and is in the same folder as the script
coco_file_path = pathlib.Path("C:/Users/v-robertorom/Documents/Python Scripts/CV/test_coco.json")
annotation_kind = AnnotationKind.OBJECT_DETECTION # or AnnotationKind.OBJECT_DETECTION
purpose = Purpose.EVALUATION # or Purpose.EVALUATION

check_coco_annotation_file(json.loads(coco_file_path.read_text()), annotation_kind, purpose)
print("Data validation passed.")