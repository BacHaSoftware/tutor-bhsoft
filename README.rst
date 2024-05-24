Installation
------------

Check to see if the folder exists::

    cd "$(tutor plugins printroot)"

If it doesn't exit, create it::

    mkdir "$(tutor plugins printroot)"


Continue::

    cd "$(workspace)"
    git clone https://github.com/BacHaSoftware/tutor-bhsoft.git
    pip install -e tutor-bhsoft
    tutor plugins enable bhsoft
    tutor config save

Rebuild MFE image::

    tutor images build mfe


Update
------------

tutor plugins update bhsoft


Docker
Kill all docker instances::
    killall Docker && open /Applications/Docker.app