# grab arguments
save_dir=$1
url_alongtrack="https://tds.aviso.altimetry.fr/thredds/dodsC/2020a-SSH-mapping-NATL60-along-track"

wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_jason1.nc"
