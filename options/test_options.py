import argparse

class TestOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.initialize()

    def initialize(self):
        self.parser.add_argument('--eval_data', type=str, required=True, help='Dataset to evaluate')
        self.parser.add_argument('--dataroot_dpdd', type=str, default='./datasets/DPDD')
        self.parser.add_argument('--dataroot_rf', type=str, default='./datasets/RealDOF')
        self.parser.add_argument('--dataroot_pixeldp', type=str, default='./datasets/PixelDP')
        self.parser.add_argument('--dataroot_cuhk', type=str, default='./datasets/CUHK')
        self.parser.add_argument('--results_dir', type=str, default='./results', help='results directory')
        self.parser.add_argument('--net_mode', type=str, default='single', choices=['single', 'dual'], help='Network mode: single or dual')
        self.parser.add_argument('--name', type=str, default='experiment_name', help='Name of the experiment')
        self.parser.add_argument('--save_images', action='store_true', help='Save output images')
        self.parser.add_argument('--custom_data_path', type=str, default='', help='Path to custom dataset')
        
    def parse(self):
        self.opt = self.parser.parse_args()
        return self.opt
