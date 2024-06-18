Installation
------------

Check to see if the folder exists::

    cd "$(tutor plugins printroot)"

If it doesn't exit, create it::

    mkdir "$(tutor plugins printroot)"


Install MFE python plugins::

    cd "$(workspace)"
    git clone https://github.com/BacHaSoftware/tutor-bhsoft.git
    pip install -e tutor-bhsoft
    tutor plugins enable bhsoft
    tutor config save

Install MFE yml plugins::

    cd "$(workspace)"
    cp home-mfe.yml $(tutor plugins printroot)
    cp course-about-mfe.yml $(tutor plugins printroot)
    tutor plugins enable landing-mfe
    tutor plugins enable course-about-mfe

Verify installed plugins::
    tutor plugins list

Update plugins::

    tutor plugins update bhsoft
    tutor plugins update landing-mfe
    tutor plugins update lcourse-about-mfe

Rebuild MFE image::

    tutor images build mfe
    tutor images build mfe  --no-cache --no-registry-cache

Remove docker buildx::

    docker buildx rm singlecpu

Create docker buildx::

    docker buildx create --use --name=singlecpu --config=./buildkitd.toml
