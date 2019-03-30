#!/usr/bin/env bash
# Push a new version of the library to PyPi

python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

echo "Does everything look OK?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) twine upload dist/*; break;;
        No ) exit;;
    esac
done
