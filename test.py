from model.data_utils import CoNLLDataset, minibatches
from model.config import Config


if __name__ == '__main__':

    # config = Config()
    #
    # train = CoNLLDataset(config.filename_train, config.processing_word,
    #                      config.processing_tag, config.max_iter)
    #
    # batch_size = config.batch_size
    # for i, (words, labels, masks) in enumerate(minibatches(train, batch_size)):
    #     print(masks)
    #     for word in words:
    #         for i in word:
    #             print(i)
    #     # print(labels)
    #     break


    with open("data/enwiki_match_title.txt") as f:
        i = 0
        for line in f:
            if "None" in line:
                i += 1
        print(i)


