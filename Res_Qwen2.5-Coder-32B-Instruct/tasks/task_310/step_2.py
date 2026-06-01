import os
import cv2
import numpy as np

image_files = [
    "./cpython/InternalDocs/images/python-cyclic-gc-4-new-page.png",
    "./cpython/InternalDocs/images/python-cyclic-gc-3-new-page.png",
    "./cpython/InternalDocs/images/python-cyclic-gc-2-new-page.png",
    "./cpython/InternalDocs/images/python-cyclic-gc-1-new-page.png",
    "./cpython/InternalDocs/images/python-cyclic-gc-5-new-page.png",
    "./cpython/PC/icons/logox128.png",
    "./cpython/PC/icons/py.png",
    "./cpython/PC/icons/pythonwx150.png",
    "./cpython/PC/icons/pythonx44.png",
    "./cpython/PC/icons/pythonx150.png",
    "./cpython/PC/icons/idlex44.png",
    "./cpython/PC/icons/pythonwx44.png",
    "./cpython/PC/icons/idlex150.png",
    "./cpython/PC/icons/pythonx50.png",
    "./cpython/Mac/BuildScript/resources/background.jpg",
    "./cpython/Objects/object_layout_313.png",
    "./cpython/Objects/object_layout_full_312.png",
    "./cpython/Objects/object_layout_full_313.png",
    "./cpython/Objects/object_layout_312.png",
    "./cpython/Lib/test/test_email/data/python.jpg",
    "./cpython/Lib/test/test_email/data/python.png",
    "./cpython/Lib/test/tkinterdata/python.png",
    "./cpython/Lib/profiling/sampling/_assets/python-logo-only.png",
    "./cpython/Lib/profiling/sampling/_assets/tachyon-logo.png",
    "./cpython/Lib/idlelib/Icons/idle_256.png",
    "./cpython/Lib/idlelib/Icons/idle_16.png",
    "./cpython/Lib/idlelib/Icons/idle_48.png",
    "./cpython/Lib/idlelib/Icons/idle_32.png",
    "./cpython/Doc/_static/og-image.png",
    "./cpython/Doc/library/hashlib-blake2-tree.png",
    "./cpython/Doc/library/tachyon-heatmap.png",
    "./cpython/Doc/library/pathlib-inheritance.png",
    "./cpython/Doc/library/tk_msg.png",
    "./cpython/Doc/library/tachyon-flamegraph.png",
    "./cpython/Doc/library/kde_example.png",
    "./cpython/Doc/library/tachyon-gecko-calltree.png",
    "./cpython/Doc/library/tachyon-pstats.png",
    "./cpython/Doc/library/turtle-star.png",
    "./cpython/Doc/library/tachyon-heatmap-with-opcodes.png",
    "./cpython/Doc/library/tachyon-gecko-flamegraph.png",
    "./cpython/Doc/library/tachyon-gecko-opcodes.png",
    "./cpython/Doc/using/mac_installer_05_custom_install.png",
    "./cpython/Doc/using/mac_installer_04_installation_type.png",
    "./cpython/Doc/using/mac_installer_08_install_certificates.png",
    "./cpython/Doc/using/mac_installer_01_introduction.png",
    "./cpython/Doc/using/mac_installer_09_custom_install_free_threaded.png",
    "./cpython/Doc/using/mac_installer_06_summary.png",
    "./cpython/Doc/using/win_install_freethreaded.png",
    "./cpython/Doc/using/win_installer.png",
    "./cpython/Doc/using/mac_installer_03_license.png",
    "./cpython/Doc/using/mac_installer_07_applications.png",
    "./cpython/Doc/using/mac_installer_02_readme.png",
    "./cpython/Doc/howto/logging_flow.png",
    "./cpython/Tools/msi/bundle/SideBar.png",
    "./cpython/Platforms/Android/testbed/app/src/main/res/drawable-xxhdpi/ic_launcher.png",
    "./requests/docs/_static/requests-sidebar.png",
    "./requests/ext/requests-logo.png",
    "./requests/ext/kr.png",
    "./requests/ext/requests-logo-compressed.png",
    "./requests/ext/psf.png"
]

def compute_histogram(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()