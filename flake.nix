{
  description = "ArcFace face recognition algorithm implementation for TensorFlow Lite";

  inputs = {
    nixpkgs.url = github:nixos/nixpkgs/nixos-unstable;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = { self, nixpkgs, flake-utils }:
  flake-utils.lib.eachSystem [ "x86_64-linux" "aarch64-linux" ] (system:
  let
    pkgs = import nixpkgs { inherit system; };
    model-url = "https://cloud.ins.jku.at/index.php/s/g2YDT8Zn9RkzsEy/download";
    model-file = builtins.fetchurl {
      url = model-url;
      sha256 = "1vqvabkcada770mqyaxa91bhd24zaqam48n8z7fi76j7mf3sf3kh";
    };
    pythonPackages = pkgs.python39Packages;
  in {

    packages.arcface-tflite = pythonPackages.buildPythonPackage {
      pname = "arcface";
      version = "0.0.8";
      src = ./.;
      checkInputs = with pythonPackages; [ pytest pytest-runner astropy ];
      preCheck = ''
        tmp_dir=$(mktemp -d)
        model_dir="$tmp_dir/.astropy/cache/download/url/${builtins.hashString "md5" model-url}"
        mkdir -p $model_dir
        cp ${model-file} "$model_dir/contents"
        echo -n "${model-url}" > "$model_dir/url"
        export HOME=$tmp_dir
      '';
      # stop pathcing opencv package name once this is fixed: https://github.com/NixOS/nixpkgs/issues/157397
      postPatch = ''
        sed -i 's/opencv-python/opencv/' setup.py
      '';
      propagatedBuildInputs = with pythonPackages; [ numpy pyyaml tensorflow keras opencv4 ];
      meta = with pkgs.lib; {
        homepage = "https://github.com/mobilesec/arcface-tensorflowlite";
        license = licenses.eupl12;
      };
    };

    defaultPackage = self.packages.${system}.arcface-tflite;
  });
}
