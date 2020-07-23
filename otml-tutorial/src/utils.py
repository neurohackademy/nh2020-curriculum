import mne
from numba import jit

@jit(nogil=True, cache=True, nopython=True)
def floyd_warshall(dist):
    npoints = dist.shape[0]
    for k in range(npoints):
        for i in range(npoints):
            for j in range(npoints):
                # If i and j are different nodes and if
                # the paths between i and k and between
                # k and j exist, do
                # d_ikj = min(dist[i, k] + dist[k, j], dist[i, j])
                d_ikj = dist[i, k] + dist[k, j]
                if ((d_ikj != 0.) and (i != j)):
                    # See if you can't get a shorter path
                    # between i and j by interspacing
                    # k somewhere along the current
                    # path
                    if ((d_ikj < dist[i, j]) or (dist[i, j] == 0)):
                        dist[i, j] = d_ikj
    return dist


def mesh_all_distances(points, tris, verts=None):
    """Compute all pairwise distances on the mesh based on edges lengths
    using Floyd-Warshall algorithm
    """
    A = mne.surface.mesh_dist(tris, points)
    if verts is not None:
        A = A[verts][:, verts]
    A = A.toarray()
    A[A == 0.] = 1e6
    A.flat[::len(A) + 1] = 0.
    print('Running Floyd-Warshall algorithm to compute distances...')
    A = floyd_warshall(A)
    return A


def get_surface(spacing, subjects_dir):
    print('Computing source space ...')
    src = mne.setup_source_space(subject="fsaverage",
                                 spacing=spacing,
                                 subjects_dir=subjects_dir,
                                 add_dist=False,
                                 verbose=False)
    tris = src[0]["use_tris"]
    vertno = src[0]["vertno"]
    points = src[0]["rr"][vertno]
    return points, tris

def get_surf_dist(spacing, subjects_dir):
    surf = get_surface(spacing, subjects_dir)
    dist = mesh_all_distances(*surf)
    print('Done!')
    return surf, dist
