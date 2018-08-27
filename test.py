from model.data_utils import CoNLLDataset, minibatches
from model.config import Config


if __name__ == '__main__':

    config = Config()

    train = CoNLLDataset(config.filename_train, config.processing_word,
                         config.processing_tag, config.max_iter)

    batch_size = config.batch_size
    for i, (words, labels, masks) in enumerate(minibatches(train, batch_size)):
        print(masks)
        print(i)


