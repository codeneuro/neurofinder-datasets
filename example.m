% example MATLAB script for loading neurofinder data
%
% for more info see:
%
% - http://neurofinder.codeneuro.org
% - https://github.com/codeneuro/neurofinder
%
% requires two packages from the matlab file exchange
%
% - recursive directory listing 
% - http://www.mathworks.com/matlabcentral/fileexchange/32226-recursive-directory-listing-enhanced-rdir
%
% - jsonlab
% - http://www.mathworks.com/matlabcentral/fileexchange/33381-jsonlab--a-toolbox-to-encode-decode-json-files-in-matlab-octave
%

% load the images
files = rdir('images/*.tiff');

for i = 1:length(files)
	imgs(:,:,i) = imread(files(i).name);
end
[x, y, z] = size(imgs)

% load the regions (training data only)
regions = loadjson('regions/regions.json');
masks = zeros(x, y);

for i = 1:length(regions)
	if isstruct(regions)
		coords = regions(i).coordinates;
	elseif iscell(regions)
		coords = regions{i}.coordinates;
	end
	masks(sub2ind([x, y], coords(:,1), coords(:,2))) = 1;
end

% show the outputs
figure();
subplot(1,2,1);
imagesc(mean(imgs,3)); colormap('gray'); axis image off;
subplot(1,2,2);
imagesc(masks); colormap('gray'); axis image off;