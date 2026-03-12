import os
import urllib.request as request
import zipfile
import tensorflow as tf
import time
from CNN_Classifier.config.configuration import PrepareCallbackConfig

class PrepareCallback:
    def __init__(self, config: PrepareCallbackConfig):
        self.config = config

    @property
    def _create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_log_dir, 
            f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_callbacks(self):
        return [
            self._create_tb_callback,
            self._create_ckpt_callback  
        ] 