from benchmark import Benchmark
from datageneration import DatasetGenerator

# configuration #1 (Windows)
int_image_dir = "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2\\int" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/int"
seg_image_dir = "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2\\seg" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/seg"
work_dir = "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_work_dir"
nyxus_executable = "/is/not/used"	# Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus/build_man/nyxus"
feature_list = "/is/not/used"	# samee--> "*ALL*"
generate_missing_image = False
base_mask_image_path = "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2\\arnoldcat_pure_cat.jpg" # Samee-->  "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/arnoldcat_pure_cat.jpg"
base_intensity_image_path = "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2\\siemens_star.tif" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/Siemens_star.tif"

# configuration #2 (EC2)
'''
int_image_dir = "/home/ec2-user/work/data/synthetic2/int"	# Windows--> "E:\\WORK-AXLE\\SYNTHETIC2\\int" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/int"
seg_image_dir = "/home/ec2-user/work/data/synthetic2/seg"	# Windows--> "E:\\WORK-AXLE\\SYNTHETIC2\\seg" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/seg"
work_dir = "/home/ec2-user/work/data/synthetic2"	# Windows--> "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_work_dir"
nyxus_executable = "/is/not/used"	# Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus/build_man/nyxus"
feature_list = "*ALL*"
generate_missing_image = False
base_mask_image_path = "/home/ec2-user/work/data/synthetic2/arnoldcat_pure_cat.jpg"	# Windows--> "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2\\arnoldcat_pure_cat.jpg" # Samee-->  "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/arnoldcat_pure_cat.jpg"
base_intensity_image_path = "/home/ec2-user/work/data/synthetic2/siemens_star.tif"	# Windows--> "C:\\WORK\\AXLE\\paper2022\\scalability-samee\\SYNTHETIC2\\siemens_star.tif" # Samee--> "/home/samee/axle/dev/nyxus_paper/nyxus_benchmark/Siemens_star.tif"
'''

if __name__ == '__main__':

    dataset_generator = DatasetGenerator(   int_image_dir,
                                            seg_image_dir,
                                            base_mask_image_path,
                                            base_intensity_image_path)

    n_rois = [100] ### [10, 50, 100, 500, 1000, 10000, 100000, 500000, 1000000]	# Smaller first
    #---	n_rois = [1000000, 500000, 100000, 10000, 1000, 500, 100, 50, 10]	# Larger first

    roi_areas = [10000] ### [10, 100, 500, 1000, 10000, 100000, 1000000]	# Smaller first
    #---	roi_areas = [1000000, 100000, 10000, 1000, 500, 100, 10]	# Larger first
    
    padding = 5
    percent_oversized_roi = 30

    for n_roi in n_rois:
        for roi_size in roi_areas:
            print ("generating n_roi={0} roi_size={1} \n".format(n_roi, roi_size))
            dataset_generator.generate_image_pair(n_roi ,roi_size, padding, percent_oversized_roi)

    '''
    benchmark = Benchmark(  int_image_dir,
                            seg_image_dir,
                            work_dir, 
                            nyxus_executable, 
                            feature_list, 
                            generate_missing_image
                        )


    benchmark.run_benchmark_suit()
    benchmark.create_benchmark_plot("Total", "All", "All")
    '''
	