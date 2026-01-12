**B.6 FreeCAD**
===================================

**[1t]** FreeCAD
----------------------------------------------

.. raw:: html

    <hr>

.. code-block:: python

  Create your FreeCAD Python script (e.g., my_script.py) containing the FreeCAD
  API calls as if it were a macro. Use Pythons subprocess module to execute the
  freecadcmd (or FreeCAD.exe --console or similar, depending on OS) executable,
  passing your script as an argument. Example Script: python import subprocess
  import os

  # Define the path to the freecadcmd executable or AppImage
  # Adjust this path based on your installation
  # Example Linux: FC_PATH = '/usr/bin/freecadcmd'
  # Example Windows: FC_PATH = 'C:\\Program Files\\FreeCAD X.YY\\bin\\freecadcmd.exe'
  # Example AppImage: FC_PATH = '~/Downloads/FreeCAD_*.AppImage' 

  FC_PATH = 'freecadcmd' # Try this if the executable is in your system PATH

  script_to_run = 'my_script.py' # Your automation script

  try:
      # Run FreeCAD in no-GUI/console mode, executing the script
      result = subprocess.run([FC_PATH, script_to_run], capture_output=True, text=True, check=True)
      print("Script ran successfully.")
      print("Output:\n", result.stdout)
  except FileNotFoundError:
      print(f"Error: FreeCAD executable not found at '{FC_PATH}'. Check your path.")
  except subprocess.CalledProcessError as e:
      print("Error running FreeCAD command.")
      print("STDOUT:", e.stdout)
      print("STDERR:", e.stderr)