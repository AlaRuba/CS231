load mnist_uint8;
N_CLASSES = 4;
size(train_y)
train_y = [];
train_x = [];
test_x = [];
test_y = [];
folder = uigetdir; % check the help for uigetdir to see how to specify a starting path, which makes your life easier 
chagall_x = [];
chagall_y = [];
% get the names of all files. dirListing is a struct array. 
dirListing = dir(folder); 
%chagall
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
        image = reshape(image, 768,[],1);
        chagall_x = cat(3, chagall_x, image);
        y = zeros(1,N_CLASSES);
        y(1,1) = 1;
        chagall_y = vertcat(chagall_y, y);
    end
% do something 
% if-clause 
end % for-loop
s = 1:40;
s=s(randperm(length(s)));
train_x = cat(3, train_x, chagall_x(:,:,s(1:24)));
train_y = vertcat(train_y, chagall_y(s(1:24),:));
test_x = cat(3, test_x, chagall_x(:,:,s(25:40)));
test_y = vertcat(test_y, chagall_y(s(25:40),:));

folder = uigetdir; % check the help for uigetdir to see how to specify a starting path, which makes your life easier 
%kand
kand_x = [];
kand_y = [];
% get the names of all files. dirListing is a struct array. 
dirListing = dir(folder); 
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
        image = reshape(image, 768,[],1);
        kand_x = cat(3, kand_x, image);
        y = zeros(1,N_CLASSES);
        y(1,2) = 1;
        kand_y = vertcat(kand_y, y);
    end
end
size(kand_x)
s = 1:400;
s=s(randperm(length(s)));

kand_x = kand_x(:,:,1:400);
kand_y = kand_y(1:400,:);
train_x = cat(3, train_x, kand_x(:,:,s(1:240)));
train_y = vertcat(train_y, kand_y(s(1:240),:));
test_x = cat(3, test_x, kand_x(:,:,s(250:400)));
test_y = vertcat(test_y, kand_y(s(250:400),:));

folder = uigetdir; % check the help for uigetdir to see how to specify a starting path, which makes your life easier 
%kand
klimt_x = [];
klimt_y = [];
% get the names of all files. dirListing is a struct array. 
dirListing = dir(folder); 
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
        image = reshape(image, 768,[],1);
        klimt_x = cat(3, klimt_x, image);
        y = zeros(1,N_CLASSES);
        y(1,3) = 1;
        klimt_y = vertcat(klimt_y, y);
    end
end
size(klimt_x)
s = 1:130;
s=s(randperm(length(s)));

klimt_x = klimt_x(:,:,1:130);
klimt_y = klimt_y(1:130,:);
train_x = cat(3, train_x, klimt_x(:,:,s(1:78)));
train_y = vertcat(train_y, klimt_y(s(1:78),:));
test_x = cat(3, test_x, klimt_x(:,:,s(79:130)));
test_y = vertcat(test_y, klimt_y(s(79:130),:));

folder = uigetdir; % check the help for uigetdir to see how to specify a starting path, which makes your life easier 
%kand
mond_x = [];
mond_y = [];
% get the names of all files. dirListing is a struct array. 
dirListing = dir(folder); 
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
        image = reshape(image, 768,[],1);
        mond_x = cat(3, mond_x, image);
        y = zeros(1,N_CLASSES);
        y(1,4) = 1;
        mond_y = vertcat(mond_y, y);
    end
end
size(mond_x)
s = 1:70;
s=s(randperm(length(s)));

mond_x = mond_x(:,:,1:70);
mond_y = mond_y(1:70,:);
train_x = cat(3, train_x, mond_x(:,:,s(1:42)));
train_y = vertcat(train_y, mond_y(s(1:42),:));
test_x = cat(3, test_x, mond_x(:,:,s(43:70)));
test_y = vertcat(test_y, mond_y(s(42:70),:));
size(train_x)


%train_x = double(reshape(train_x',28,28,60000))/255;
%test_x = double(reshape(test_x',28,28,10000))/255;
train_x = double(train_x)/255;
test_x = double(test_x)/255;
train_y = double(train_y');
test_y = double(test_y');
size(train_y)
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
opts.batchsize = 48;
opts.numepochs = 1;
size(images,3)
cnn = cnntrain(cnn, train_x, train_y, opts);

[er, bad] = cnntest(cnn, test_x, test_y);

%plot mean squared error
figure; plot(cnn.rL);