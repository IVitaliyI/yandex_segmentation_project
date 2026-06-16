from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class TrainDatasetForStudents(BaseSegDataset):
    METAINFO = dict(
        classes=('background', 'cat', 'dog'),
        palette=[[0, 0, 0], [255, 0, 0], [0, 255, 0]]
    )
    def __init__(
        self,      
        ann_file = '', 
        img_suffix='.jpg', 
        seg_map_suffix='.png', 
        metainfo = None, 
        data_root = None, 
        data_prefix = ..., 
        filter_cfg = None, 
        indices = None, 
        serialize_data = True, 
        pipeline = ..., 
        test_mode = False, 
        lazy_init = False, 
        max_refetch = 1000, 
        ignore_index = 255, 
        reduce_zero_label = False, 
        backend_args = None
    ):
        super().__init__(
            ann_file, 
            img_suffix,
            seg_map_suffix, 
            metainfo, 
            data_root, 
            data_prefix, 
            filter_cfg, 
            indices, 
            serialize_data, 
            pipeline, 
            test_mode, 
            lazy_init, 
            max_refetch, 
            ignore_index, 
            reduce_zero_label,
            backend_args
        )