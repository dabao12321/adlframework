from adlframework._dataentity import DataEntity
import arff
import numpy as np
from adlframework.utils import get_logger

logger = get_logger()

class ARFFDataEntity(DataEntity):
    '''
    Represents a arff file.
    '''

    def _read_file(self):
        """
        Receives a file path from retrieval and loads/returns data.
        """
        f = self.retrieval.get_data(self.unique_id)
        self.data = np.array([x for x in arff.load(f)])
        return self.data

    def get_sample(self):
        '''
            Given a numpy array of returned sample, it returns a sample.
        '''
        if self.labels is None: # Read labels into memory.
            self.label = self.retrieval.get_label(self.unique_id).iloc[0]
        if self.data is None: # Read data into memory.
            self.get_data()
        return self.data, self.label
        
