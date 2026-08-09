#!/bin/bash
msg="${1:-Update meme storage [skip ci]}"
git add meme_storage.json
git commit -m "$msg"
git push