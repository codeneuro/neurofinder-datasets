// example node.js script for loading neurofinder data
// 
// for more info see:
//
// - http://neurofinder.codeneuro.org
// - https://github.com/codeneuro/neurofinder
//
// requires a few node modules, install with `npm install <module>`
//
// "ndarray": "^1.0.18",
// "ndarray-imshow": "^1.0.1",
// "ndarray-ops": "^1.2.2",
// "progress": "^1.1.8",
// "tiff": "^1.1.0",
// "zeros": "^1.0.0"
//

var fs = require('fs')
var tiff = require('tiff')
var progress = require('progress')
var zeros = require('zeros')
var ndarray = require('ndarray')
var ops = require('ndarray-ops')
var imshow = require('ndarray-imshow')

// load images
var sum, mat, image, buffer
var files = fs.readdirSync('images')
var bar = new progress('loading [:bar] :percent :etas', { total: files.length , width: 50})

files.forEach(function (file, index) {
  buffer = fs.readFileSync('images/' + file)
  image = new tiff.TIFFDecoder(buffer).decode().ifd[0]
  mat = ndarray(image.data, [image.width, image.height])
  if (!sum) sum = zeros([image.width, image.height])
  ops.add(sum, mat, sum)
  bar.tick()
})

// load regions
var blob = JSON.parse(fs.readFileSync('regions/regions.json'))
var regions = blob.map(function (region) {return region.coordinates})
var mask = zeros(sum.shape)
regions.forEach(function (region) {
  region.forEach(function (coordinate) {
    mask.set(coordinate[0], coordinate[1], 1)
  })
})

// show the outputs
imshow(sum, {colormap: 'gray'})
imshow(mask, {colormap: 'gray'})
