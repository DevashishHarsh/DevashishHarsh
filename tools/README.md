# Profile display assets

`python3 tools/build_profile.py` regenerates the mobile console and four desktop project displays using standard-library SVG generation. All typography, diagrams, monitor housing and TOB geometry are local vector assets. No private company models or third-party badge services are used.

The profile uses `assets/lab-display.gif` for its desktop rotation, `assets/lab-display.svg` for reduced-motion preferences, and `assets/lab-console-mobile.svg` on small screens. The GIF contains four 900 × 623 project frames, held for eight seconds each, then loops. It is a portfolio illustration rather than a recording of project execution.

To refresh the GIF after a visual change, render the four `lab-display-N.svg` files at 900 pixels wide in a browser, then encode the frames as a GIF with an eight-second duration per frame and looping enabled. The native Markdown links below the display open the repositories; project details remain available as selectable text in the README.

The previous banner assets remain in the assets directory but are no longer referenced by the profile README.
