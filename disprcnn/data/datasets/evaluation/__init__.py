from disprcnn.data import datasets

from .kitti import kitti_evaluation


def evaluate(dataset, predictions, output_folder, **kwargs):
    """evaluate dataset using different methods based on dataset type.
    Args:
        dataset: Dataset object
        predictions(dict(list[BoxList])): each item in the list represents the
            prediction results for one image.
        output_folder: output folder, to save evaluation files or results.
        **kwargs: other args.
    Returns:
        evaluation result
    """
    args = dict(
        dataset=dataset,
        left_predictions=predictions['left'],
        right_predictions=predictions['right'],
        output_folder=output_folder, **kwargs
    )
    if isinstance(dataset, (
            datasets.KITTIObjectDatasetPOB, datasets.KITTIObjectDatasetVOB)):
        return kitti_evaluation(**args)

    else:
        dataset_name = dataset.__class__.__name__
        raise NotImplementedError("Unsupported dataset type {}.".format(dataset_name))
