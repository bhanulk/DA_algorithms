import pandas as pd
import  math
import  numpy as np
import matplotlib.pyplot

df= pd.read_csv('kmeans.csv')
k=int(input('enter the number of clusters:'))
data_points=df.values
print(data_points)

def intialize_centroids(data,k):
    indices = np.random.choice(data.shape[0], k, replace=False) 
    return data[indices]  


def assign_clusters(data,centroids):
    clusters={}
    for i in range(k):
        clusters[i]=[]

    for  points in data:
        distance=[np.linalg.norm(points-centroid)for centroid in centroids]
        cluster_id=distance.index(min(distance))
        clusters[cluster_id].append(points)
    return clusters

def update_centroids (clusters):
    centroids=[]
    for key in clusters.keys():
        centroid=np.mean(clusters[key],axis=0)
        centroids.append(centroid)
    return centroids

def converged(old_centroids,centroids):
    distances = [np.linalg.norm(old_centroids[i] - centroids[i]) for i in range(len(centroids))]
    return sum(distances) == 0

def kmeans(data,k):
    centroids= intialize_centroids(data,k)
    old_centroids=None
    iterations=0
    
    while old_centroids is None or not converged(old_centroids,centroids):
        clusters=assign_clusters(data,centroids)
        print(f"iteration{iterations+1}")

        for clusterid,points in clusters.items():
            print(f"Cluster {clusterid}:{points}")
        
        old_centroids=centroids
        centroids=update_centroids(clusters)
        iterations+=1
    return clusters,centroids

clusters, centroids = kmeans(data_points, k)

print("\nFinal clusters:")
for cluster_id, cluster_points in clusters.items():
    print(f"Cluster {cluster_id + 1}: {cluster_points}")

print("\nFinal centroids:", centroids)


