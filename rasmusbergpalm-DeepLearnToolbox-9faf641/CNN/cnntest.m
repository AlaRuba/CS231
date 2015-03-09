function [er, bad] = cnntest(net, x, y)
    %  feedforward
    disp('size of net')
    size(net)
    disp('size of x')
    size(x)
    net = cnnff(net, x);
    [~, h] = max(net.o);
    [~, a] = max(y);
    bad = find(h ~= a);

    er = numel(bad) / size(y, 2);
end
