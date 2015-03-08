load mnist_uint8;

size(train_x)
folder = uigetdir; % check the help for uigetdir to see how to specify a starting path, which makes your life easier 

% get the names of all files. dirListing is a struct array. 
dirListing = dir(folder); 

% loop through the files and open. Note that dir also lists the directories, so you have to check for them. 
for d = 1:length(dirListing) 
    fileName = fullfile(folder,dirListing(d).name);
    isImg = false;
    fileName;
    try
    % imfinfo errors out if file isn't in a format
    % it recognizes, so put the call in a try-catch.
        
        isImg = strfind(fileName, '.png');
        if size(isImg,1) < 1
            isImg = false;
        else
            isImg = true;
        end
    catch
        isImg = false;
    end
    if isImg == true
% open your file here 
        image = imread(fileName);
        image = reshape(image, )
        size(image)
    end
% do something 

 % if-clause 
end % for-loop
train_x = double(reshape(train_x',28,28,60000))/255;
test_x = double(reshape(test_x',28,28,10000))/255;
train_y = double(train_y');
test_y = double(test_y');
size(train_x)
%% ex1 Train a 6c-2s-12c-2s Convolutional neural network 
%will run 1 epoch in about 200 second and get around 11% error. 
%With 100 epochs you'll get around 1.2% error
rand('state',0)
cnn.layers = {
    struct('type', 'i') %input layer
    struct('type', 'c', 'outputmaps', 6, 'kernelsize', 5) %convolution layer
    struct('type', 's', 'scale', 2) %sub sampling layer
    struct('type', 'c', 'outputmaps', 12, 'kernelsize', 5) %convolution layer
    struct('type', 's', 'scale', 2) %subsampling layer
};
cnn = cnnsetup(cnn, train_x, train_y);

opts.alpha = 1;
opts.batchsize = 50;
opts.numepochs = 1;

cnn = cnntrain(cnn, train_x, train_y, opts);

[er, bad] = cnntest(cnn, test_x, test_y);

%plot mean squared error
figure; plot(cnn.rL);