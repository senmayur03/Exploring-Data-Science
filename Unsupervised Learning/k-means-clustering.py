import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.datasets import make_blobs

# Create random clustered data points.
X, y = make_blobs(
    n_samples = 150, n_features = 2,
    centers = 3, cluster_std = 0.5, 
    shuffle = True, random_state = 0
)
def random_hex_color():
    hex_values = "123456789ABCDEF"
    hex_value = "#"
    for _ in range(6):
        hex_value = hex_value + random.choice(hex_values)
    return hex_value

# Convert a numpy array into a list of tuples.
def convert_array_to_tuples(numpy_array):
    tuple_list = list(map(tuple, numpy_array))
    return tuple_list

# Calculate the squared euclidean distance between two points.
def squared_euclidean_distance(point_1, point_2):
    distance = ((point_2[0] - point_1[0]) ** 2) + ((point_2[1] - point_1[1]) ** 2)
    return distance

# Return the closest point in a list compared to an initial point.
def least_squared_euclidean_distance(point_list, point_1):
    closest_point = None
    closest_distance = float("inf")
    for point in point_list:
        distance = squared_euclidean_distance(point_1, point)
        if distance < closest_distance:
            closest_point = point
            closest_distance = distance
    return closest_point

# Calculate the average point in a list of points.
def average_point(point_list):
    x_average = 0
    y_average = 0
    for point in point_list:
        x_average = x_average + point[0]
        y_average = y_average + point[1]
    x_average = x_average / len(point_list)
    y_average = y_average / len(point_list)

    return (x_average, y_average)

def check_similarity(old_centroids, new_centroids):
    similarity = 0
    for i in range(len(old_centroids)):
        similarity = similarity + ((old_centroids[i] - new_centroids[i]) / old_centroids[i])
    similarity = similarity / range(len(old_centroids))
    return new_centroids

# Display the clusters on a plot including the centroid
def display_clusters(centroid_dict, centroids):
    centroid_list = np.array(list(map(np.array, centroids)))
    cluster_list = []

    for centroid in centroids:
        cluster = np.array(list(map(np.array, centroid_dict[centroid])))
        cluster_list.append(cluster)

    for cluster in cluster_list:
        plt.scatter(
            cluster[:, 0], cluster[:, 1],
            s=50, c=random_hex_color(),
            marker='s', edgecolor='black',
            label='cluster 1'
        )
    plt.scatter(
        centroid_list[:, 0], centroid_list[:, 1],
        s=250, marker='*',
        c='red', edgecolor='black',
        label='centroids'
    )
    plt.show()

def k_means_clustering(data_points, number_of_centroids):
    tuple_list = convert_array_to_tuples(data_points)
    # Randomly select n number of centroids.
    centroids = random.sample(tuple_list, number_of_centroids)
    # A dictionary containing a centroid as key.
    # A list of datapoints associated with that centroid as value.
    centroid_dict = {}

    old_centroids = []

    # Currently set to 10 iterations.
    for _ in range(10):
        # Empty the dictionary and store the new centroids.
        centroid_dict = {}
        for centroid in centroids:
            centroid_dict[centroid] = []
        # For each data point, calculate the closest centroid and store it in the respective list.
        for data_point in tuple_list:
            closest_centroid = least_squared_euclidean_distance(centroids, data_point)
            centroid_dict[closest_centroid].append(data_point)
        # Calculate the new centroids by averaging each list of points and update the list of centroids.
        new_centroids = []
        for point_list in centroid_dict.values():
            new_centroids.append(average_point(point_list))
        centroids = new_centroids

    # Visualise the clusters.
    display_clusters(centroid_dict, centroids)

k_means_clustering(X, 3)