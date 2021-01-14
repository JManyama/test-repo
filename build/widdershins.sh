#!/bin/bash

For /R src/api-explorer/ %G IN (*.json) do widdershins "%G" -o "%G".md