import cv2
import numpy as np
import os

# read images
def read_iamges(pa):
    pa_d = os.listdir(pa)
    im_li = []
    for fi in pa_d:
        fu_fi = pa + fi
        img = cv2.imread(fu_fi)
        im_li.append([fi, img])
    return im_li

# get the mask of Lysosome and cell membrane
def get_info(img, pixel_width, thr):
    ker = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # cell membrane mask
    cm_mask = np.mean(img, -1)
    cm_mask[cm_mask <= 250] = 0
    cm_mask[cm_mask > 250] = 1
    cm_mask_edg = cm_mask - cv2.erode(cm_mask, ker)

    # Lysosome mask
    ls_mask = img[:,:,1] - img[:,:,2]
    ls_mask[ls_mask <= thr] = 0
    ls_mask[ls_mask > thr] = 1
    ls_mask = cv2.morphologyEx(ls_mask, cv2.MORPH_OPEN, ker, iterations=1)

    ls_mask_edg = ls_mask - cv2.erode(ls_mask, ker)

    # get components
    num_labels, ls_labels = cv2.connectedComponents(ls_mask)
    ls_labels_edg = ls_labels * ls_mask_edg

    # get information
    info_li = []
    cm_ind = np.where(cm_mask_edg == 1)
    for i in range(1, np.max(ls_labels) + 1):
        i_lab = ls_labels.copy()
        i_lab[i_lab == i] = 100000
        i_lab[i_lab != 100000] = 0
        i_lab[i_lab == 100000] = 1
        i_lab_edg = i_lab * ls_mask_edg
        i_img = i_lab * (img[:,:,1] - img[:,:,2])

        # area
        are = np.sum(i_lab)

        # density
        m_v = np.max(i_img)
        a_v = np.mean(i_img[i_img != 0])
        s_v = np.std(i_img[i_img != 0])

        # distance
        i_ind = np.where(i_lab_edg == 1)
        min_dis = 1000000
        for j in range(len(i_ind[0])):
            for k in range(len(cm_ind[0])):
                x1, y1 = i_ind[0][j], i_ind[1][j]
                x2, y2 = cm_ind[0][k], cm_ind[1][k]
                dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if dis < min_dis:
                    min_dis = dis
        info_li.append([i, are*pixel_width*pixel_width, m_v, a_v, s_v, min_dis*pixel_width])

    return cm_mask, cm_mask_edg, ls_mask, ls_mask_edg, ls_labels, ls_labels_edg, info_li


# add text
def add_text(img, lab):
    for i in range(1, np.max(lab)+1):
        ind = np.where(lab == i)
        x, y = int(np.mean(ind[0])), int(np.mean(ind[1]))
        cv2.putText(img, str(i), (y, x), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1, cv2.LINE_AA)

    return img