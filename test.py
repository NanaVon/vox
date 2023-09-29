{"chunk":2}

def fileToArray(fileName):
    f = open(fileName, 'rb')
    chunks = []
    list
    while True:
        chunk = f.read(4)  
        if not chunk:
            f.close()
            return chunks
        chunks.append(chunk)

def init_dicc(NumChunkContent=None, NunChildrenChunks=None,content_expect=None ,content=None, children=None):
    return {'NumChunkContent':NumChunkContent, 'NunChildrenChunks':NunChildrenChunks, 'content_expect':content_expect, 'content': content, 'children':children}

riff = {b'VOX ':init_dicc(content_expect=b'150'), b'MAIN':init_dicc(-1, -1)}

arrayOfChunks = fileToArray('ff1.vox')

chunksParsed = []

print(arrayOfChunks)

i = 0 
print(len(arrayOfChunks))
while i < len(arrayOfChunks):
    print(riff.keys(), arrayOfChunks[i], i)
    if arrayOfChunks[i] in riff.keys():
        print('hello world')
        
        id_c = arrayOfChunks[i]
        d = {'id':id_c}
        i +=1
        for key in riff[id_c]:
            if riff[id_c][key]:
                d[key] = arrayOfChunks[i]
                i +=1:
        chunksParsed.append(d)
    else: i += 1
print(chunksParsed)
