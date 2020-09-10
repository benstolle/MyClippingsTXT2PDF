import fitz

path = "/Users/ben/Documents/books/read/clip2anno"

def passages_from_My_Clippingstxt():
    # import My Clippings.txt to Clippings.io
    # export from Clippings.io as txt with all possible checkboxes unchecked

    passages = []
    with open(f"{path}/clippings.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line != "\n":
                passages.append(line)
    return passages

def annotate(text_passages):
    doc = fitz.open("/Users/ben/Documents/books/read/clip2anno/china.pdf")
    inst_counter = 0
    
    for passage in text_passages:
        for pi in range(doc.pageCount):
            page = doc[pi]

            text = passage
            text_instances = page.searchFor(text)

            five_percent_height = (page.rect.br.y - page.rect.tl.y)*0.05

            for inst in text_instances:
                inst_counter += 1
                highlight = page.addHighlightAnnot(inst)
                doc.save(f"{path}/china_annotated.pdf")
    doc.close()

text_passages = passages_from_My_Clippingstxt()
annotate(text_passages)