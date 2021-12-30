"""
    TOOL: Split bag files

    Usage:
    python split_bags.py --input_bagfile=<input bag file> --output_folder=<output bag folder> --n_messages_per_part=<# of messages per part>

    Eg:
    python split_bags.py --input_bagfile=data/test.bag --output_folder=data/test_split --n_messages_per_part=10000

"""
import os
import rosbag
import argparse
import math

parser = argparse.ArgumentParser(description='Split bags file info multiple parts by # of messages.')
parser.add_argument('--input_bagfile', help='Input bag file', required=True)
parser.add_argument('--output_folder', help='Output bag folder', required=True)
parser.add_argument('--n_messages_per_part', help='Number of messages per part', required=False, default=10000, type=int)
args = parser.parse_args()
    
# Get bag duration  
input_bagfile = args.input_bagfile
output_folder = args.output_folder
n_messages_per_part = int(args.n_messages_per_part)
os.system("mkdir -p {}".format(output_folder))

print("Spliting...")
input_bag = rosbag.Bag(input_bagfile)
total_messages = input_bag.get_message_count()
total_bags = int(math.ceil(total_messages / float(n_messages_per_part)))

n_bag = 0
n = 0
output_bag = rosbag.Bag(os.path.join(output_folder, "{}.bag".format(n_bag)), 'w')
print("Writing bag {} / {}".format(0, total_bags))
for topic, msg, t in input_bag.read_messages():
    # Write this image to the new file
    output_bag.write(topic, msg, t)
    n += 1
    if n >= n_messages_per_part:
        # Close the old bag
        output_bag.close()
        n_bag += 1
        print("Writing bag {} / {}".format(n_bag, total_bags))
        output_bag = rosbag.Bag(os.path.join(output_folder, "{}.bag".format(n_bag)), 'w')
        n = 0