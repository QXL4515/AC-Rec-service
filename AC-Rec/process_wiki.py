# -*- coding: utf-8 -*-
__author__ = 'huang'
 
 
import os
import logging
import sys
 
import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
from gensim.corpora import WikiCorpus
 
 
if __name__=='__main__':
 
 
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
 
 
    if len(sys.argv) < 3:
        print(globals()['__doc__'] %locals())
        sys.exit(1)
        
    inp, outp = sys.argv[1:3]
    space = ' '
    i = 0
 
 
    output = open(outp, 'w', encoding='utf-8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        data = space.join(text)
        output.write(str(data) + '\n')
        i = i + 1
        if i % 10000 == 0:
            logger.info('Saved ' + str(i) + ' articles')
 
 
    output.close()
    logger.info('Finished ' + str(i) + ' articles')