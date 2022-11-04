# grab arguments
save_dir=$1
url_alongtrack="https://tds.aviso.altimetry.fr/thredds/dodsC/2020a-SSH-mapping-NATL60-along-track"


wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_jason1.nc"
wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_envisat.nc"
wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_geosat2.nc"
wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_topex-poseidon_interleaved.nc"
wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_karin_swot.nc"
wget --directory-prefix=$save_dir $file_server"/2020a_SSH_mapping_NATL60_nadir_swot.nc"