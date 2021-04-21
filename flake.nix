{
  description = "ArcFace face recognition algorithm implementation for TensorFlow Lite";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    pypi-deps-db = {
      url = "github:DavHau/pypi-deps-db";
      flake = false;
    };
    mach-nix = {
      url = "github:DavHau/mach-nix/3.2.0";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.flake-utils.follows = "flake-utils";
      inputs.pypi-deps-db.follows = "pypi-deps-db";
    };
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, pypi-deps-db }:
  flake-utils.lib.eachSystem [ "x86_64-linux" "aarch64-linux" ] (system:
  let
    pkgs = import nixpkgs { inherit system; };
    mach-nix-utils = import mach-nix { inherit pkgs; };
    model-url = "https://cloud.ins.jku.at/index.php/s/g2YDT8Zn9RkzsEy/download";
    model-file = builtins.fetchurl {
      url = model-url;
      sha256 = "1vqvabkcada770mqyaxa91bhd24zaqam48n8z7fi76j7mf3sf3kh";
    };
  in {

    packages.arcface-tflite = mach-nix-utils.buildPythonPackage {
      src = ./.;
      extras = [ "testing" "default_model" ];
      tests = true;
      preCheck = ''
        tmp_dir=$(mktemp -d)
        model_dir="$tmp_dir/.astropy/cache/download/url/${builtins.hashString "md5" model-url}"
        mkdir -p $model_dir
        cp ${model-file} "$model_dir/contents"
        echo -n "${model-url}" > "$model_dir/url"
        export HOME=$tmp_dir
     '';
    };

    defaultPackage = self.packages.${system}.arcface-tflite;
  });
}
