scl enable rh-git29 bash
git config --global user.name "Your preferred name"
git config --global user.email "Your-Email-Address"
git config --global http.emptyAuth true
git clone --recursive https://:@gitlab.cern.ch:8443/tdr/notes/AN-18-097.git
cd AN-18-097/
utils/tdr b
