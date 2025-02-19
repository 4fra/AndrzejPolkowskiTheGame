from os import walk

import pygame


def import_folder(path):
    surf_list = []

    for _, __, img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            img_surf = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (33, 42))
            surf_list.append(img_surf)

    return surf_list
