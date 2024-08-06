{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.python39Packages.virtualenv
    pkgs.qt6.qtbase
    pkgs.qt6.qttools
    pkgs.qt6.qtsvg
    pkgs.qt6.qtdeclarative
    pkgs.qt6.qttools.dev # Ensure Qt Designer is included
  ];

  shellHook = ''
    # Create and activate a virtual environment
    if [ ! -d .venv ]; then
      python -m venv .venv
      .venv/bin/pip install --upgrade pip setuptools wheel
      .venv/bin/pip install pyside6
    fi
    source .venv/bin/activate
  '';
}
