import numpy as np
import matplotlib.pyplot as plt

# Read data from file into variables
labels, it1s, it1e, it2s, it2e, it3s, it3e, it4s, it4e = np.loadtxt(
    'mv_gantt_time.txt',
    skiprows=1, delimiter=",",
    dtype=("S20, i4, i4, i4, i4, i4, i4, i4, i4" ),
    unpack=True)

# Map value to color
color_mapper = np.vectorize(
    lambda x: {1: 'red',
               2: 'blue',
               3: 'green',
               4: 'black'}.get(x))

# Plot a line for every line of data in your file
taskn = range(1, len(labels)+1)
plt.hlines(taskn, it1s, it1e, colors="red", lw=4)
plt.hlines(taskn, it2s, it2e, colors="black", lw=4)
plt.hlines(taskn, it3s, it3e, colors="blue", lw=4)
plt.hlines(taskn, it4s, it4e, colors="green", lw=4)
#ax = plt.axes()
#start, end = ax.get_ylim()
#ax.yaxis.set_ticks(np.arange(0,max(labels)+1))
plt.yticks(taskn, labels)
plt.margins(0.1)
plt.xlabel('days')
plt.grid()
plt.savefig('gantt1.png')



#
##!/usr/bin/python
## -*- coding: utf-8 -*-
#
#import os
#import sys
#import time
#import datetime
#import shutil
#import sqlite3 as lite
#import Image as pImage
#from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
#from reportlab.platypus import XPreformatted,Table,flowables,TableStyle
#from reportlab.lib.pagesizes import letter, legal, A4, elevenSeventeen
#from reportlab.platypus.flowables import PageBreak
#from reportlab.lib.styles import getSampleStyleSheet
#from reportlab.lib import colors
#from reportlab.rl_config import defaultPageSize
#from reportlab.lib.units import inch
#from reportlab.lib.styles import ParagraphStyle
#from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT,TA_JUSTIFY
#from reportlab.pdfbase import pdfmetrics
#from reportlab.pdfbase.ttfonts import TTFont
#from reportlab.pdfbase import pdfmetrics
#from reportlab.pdfbase.ttfonts import TTFont
#
#"""generate a Reportlab PDF invoice from an sqlite database
#
#methods:
#    gen_invoice : generates invoice document
#    gen_history : generates invoice history report
#
#"""
#
## select invoice to print
#invoice_f = 'STL-0020-14'
#invoice_file = invoice_f + '.pdf'
#
## histflag = 1 prints history report
## ==================================
#histflag = 1
#history_file = 'STL-history.pdf'
#
## intialize reportlab PDF settings
## ================================
#logopath = "C:/Users/rhh/Dropbox/StructureLabs/admin/invoices/invlogo.png"
#logofile = logopath.encode('ascii','ignore')
#_sp = " "
#_nl  = "\n "
#_ns = Spacer(1,.1*inch)
## for simple doc
#_fontpath = "c:/windows/fonts/"
#_page_size = "pagesize = letter"
#_backcolor = colors.white
#_page_height = "defaultPageSize[1]"
#_page_width = "defaultPageSize[0]"
#_page_margin1 = "leftMargin = 0.75*inch, rightMargin = 0.75*inch, "
#_page_margin2 = "bottomMargin = 1.75*inch, topMargin = .3*inch, "
#_page_margin = _page_margin1 +  _page_margin2
## for canvas
#PAGE_HEIGHT = defaultPageSize [0]
#PAGE_WIDTH = defaultPageSize [0]
#
## read data from sqlite database
## ==============================
## document content
#_story1 = []  # invoice
#_story2 = []  # history
#
#if len(invoice_f) > 0:
#    invoice_no = (invoice_f,)
#    con = lite.connect('stl_invoices.sqlite')
#
#    with con:
#        cur = con.cursor()
#        cur.execute("PRAGMA foreign_keys = 1")
#
#        # write table for invoice number
#        sqlq = ("SELECT * from recip where inv_no=?")
#        cur.execute(sqlq, invoice_no)
#        data1 = cur.fetchall()
#
#        sqlq = ("SELECT * FROM inv WHERE inv_no=?")
#        cur.execute(sqlq, invoice_no)
#        data2 = cur.fetchall()
#
#    inv1 = "Invoice number: " + data1[0][0]
#    date1 = "Invoice date: " + data1[0][1]
#    name1 =     data1[0][2]
#    attn =      data1[0][3]
#    address1 =  data1[0][4]
#    city1 =     data1[0][5]
#    state1 =    data1[0][6]
#    zip1 =      data1[0][7]
#    project1 =  data1[0][8]
#    contract1 = data1[0][9]
#    paid1 =     data1[0][10]
#    note1 =     data1[0][11]
#    if note1 == None:
#        note1 =''
#    try:
#        if con:
#            con.close()
#            print("\n[invoice data selected]")
#    except:
#        print('\n[invoice data selection error]')
#
#
#if histflag == 1:
#    con = lite.connect('stl_invoices.sqlite')
#
#    with con:
#        cur = con.cursor()
#        cur.execute("PRAGMA foreign_keys = 1")
#
#        # write table for invoice number
#        sqlq = ("SELECT * from recip")
#        cur.execute(sqlq)
#        data1h = cur.fetchall()
#
#        sqlq = ("SELECT * FROM inv")
#        cur.execute(sqlq)
#        data2h = cur.fetchall()
#
#        inv2 =  data1[0][0]
#        date2 = data1[0][1]
#        name2 = data1[0][2]
#        paid2 = data1[0][10]
#        note2 = data1[0][11]
#        if note2 == None:
#            note2 =''
#    try:
#        if con:
#            con.close()
#            print("\n[history data selected]")
#    except:
#            print('\n[history data selection error]')
#
## font styles ================================================
### mono fonts
#pdfmetrics.registerFont(TTFont('vm',_fontpath + "/DejaVuSansMono.ttf"))
#pdfmetrics.registerFont(TTFont('vmi',_fontpath + "/DejaVuSansMono-Oblique.ttf"))
#pdfmetrics.registerFont(TTFont('vmb',_fontpath + "/DejaVuSansMono-Bold.ttf"))
#
### proportional fonts
#pdfmetrics.registerFont(TTFont('arial',_fontpath + "/DejaVuSans.ttf"))
#pdfmetrics.registerFont(TTFont('arialbd',_fontpath + "/DejaVuSans-Bold.ttf"))
#pdfmetrics.registerFont(TTFont('ariali',_fontpath + "/DejaVuSans-Oblique.ttf"))
#
### mono text
#_p_text = ParagraphStyle('text',alignment=TA_LEFT,
#   spaceBefore = 2, spaceAfter = 1,
#   fontSize = 10, leading = 12, fontName = 'vm',
#   leftIndent = .25 * inch, backColor = _backcolor)
#_p_textb = ParagraphStyle('text',alignment=TA_LEFT,
#   spaceBefore = 2, spaceAfter = 1,
#   fontSize = 10, leading = 12, fontName = 'vmb',
#   leftIndent = .25 * inch, backColor = _backcolor)
#_p_text4 = ParagraphStyle('text-indent1',alignment=TA_LEFT,
#   spaceBefore = 2, spaceAfter = 1,
#   fontSize = 11, leading = 12, fontName = 'vm',
#   leftIndent = .5 * inch, backColor = _backcolor)
#_p_text8 = ParagraphStyle('text-indent2',alignment=TA_LEFT,
#   spaceBefore = 2, spaceAfter = 1,
#   fontSize = 11, leading = 12, fontName = 'vm',
#   leftIndent = .75 * inch, backColor = _backcolor)
#
### arial
#_p_para1 = ParagraphStyle('basic',alignment=TA_LEFT,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 10, leading = 14, fontName = 'arial',
#   leftIndent = 0 * inch, backColor = _backcolor)
#_p_para2 = ParagraphStyle('basicbold',alignment=TA_LEFT,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 10, leading = 14, fontName = 'arialbd',
#   leftIndent = 0 * inch, backColor = _backcolor)
### italic
#_p_para3 = ParagraphStyle('basicitalic',alignment=TA_LEFT,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 10, leading = 14, fontName = 'ariali',
#   leftIndent = 0 * inch, backColor = _backcolor)
### centered
#_p_para6 = ParagraphStyle('center',alignment=TA_CENTER,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 10, leading = 14, fontName = 'arial',
#   leftIndent = 0 * inch, backColor = _backcolor)
### right aligned
#_p_para7 = ParagraphStyle('right',alignment=TA_RIGHT,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 11, leading = 14, fontName = 'arial',
#   leftIndent = 0 * inch, backColor = _backcolor)
### indented
#_p_cbold = ParagraphStyle('bold-left',alignment=TA_LEFT,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 11, leading = 14, fontName = 'arialbd',
#   leftIndent = 0 * inch, backColor = _backcolor)
#_p_cbold2 = ParagraphStyle('bold-center',alignment=TA_CENTER,
#   spaceBefore = 1, spaceAfter = 1,
#   fontSize = 12, leading = 14, fontName = 'arialbd',
#   leftIndent = 0 * inch, backColor = _backcolor)
#
#
#def gen_invoice():
#    """ generate PDF invoice
#
#    data1 and data2 are records from sqlite file
#
#    """
#    # intitialize document
#    _doc_template = "SimpleDocTemplate(invoice_file, " + _page_margin + _page_size + " )"
#    _doc = eval(_doc_template)
#    _im1 = _figure(.9,.9,'CENTER')
#    _story1.append(_im1)
#    _story1.append(_ns)
#    _story1.append(_ns)
#    _story1.append(_format('INVOICE', 4))
#
#    # heading
#    # =======
#    _story1.append(_ns)
#    _story1.append(_ns)
#    _story1.append(_ns)
#    _story1.append(_format(inv1, 0))
#    _story1.append(_ns)
#    _story1.append(_format(date1, 0))
#
#    _story1.append(_ns)
#    _story1.append(_ns)
#    _story1.append(_ns)
#    _story1.append(_format('To:', 2))
#    _story1.append(_format(name1, 0))
#    _story1.append(_format(address1, 0))
#    tmpstr = city1 + ', ' + state1 + ' ' + str(zip1)
#    _story1.append(_format(tmpstr, 0))
#
#    _story1.append(_ns)
#    _story1.append(_ns)
#    tmpstr = 'Attention: ' + attn
#    _story1.append(_format(tmpstr, 0))
#    tmpstr = 'Project: ' + project1
#    _story1.append(_format(tmpstr, 0))
#    tmpstr = 'Contract Reference: ' + contract1
#    _story1.append(_format(tmpstr, 0))
#
#    # items
#    # =====
#    _story1.append(_ns)
#    _story1.append(_ns)
#    _story1.append(_ns)
#    # table heading
#    tablehd = str('Items'.ljust(35) + 'Units'.center(15) + 'Rate($)'.center(15) + 'Amount($)'.rjust(10))
#    _story1.append(_format(tablehd, 1))
#
#    tablesep = str('_'*35 + '_'*15 + '_'*15 + '_'*10)
#    _story1.append(_format(tablesep, 1))
#    _story1.append(_ns)
#
#    # table items
#    total = 0
#    for i in data2:
#        total += i[2]*i[4]
#        row =  str(i[1].ljust(35) + repr(i[2]).rjust(5) + i[3].center(10) + repr(i[4]).rjust(5)
#                   + i[5].center(10)+ repr(i[2]*i[4]).rjust(10))
#        _story1.append(_format(row, 1))
#
#    # table total
#    tablesep = str(' '*35 + ' '*15 + ' '*15 + '_'*10)
#    _story1.append(_format(tablesep, 1))
#    _story1.append(_ns)
#    totalstr = str(' '*35 + ' '*15 + 'Total Due'.center(15) + repr(total).rjust(10))
#    _story1.append(_format(totalstr, 1))
#
#    _doc.build(_story1, onFirstPage = _firstpage, onLaterPages = _laterpages)
#
#    print("\n[invoice printed]")
#
#def gen_history():
#    """ generate PDF invoice  history
#
#    data1 and data2 are records from sqlite file
#
#    """
#    # intitialize document
#    _doc2_template = "SimpleDocTemplate(history_file, " + _page_margin + _page_size + " )"
#    _doc2 = eval(_doc2_template)
#    _im2 = _figure(.9,.9,'CENTER')
#    _story2.append(_im2)
#    _story2.append(_ns)
#    _story2.append(_ns)
#    _story2.append(_format('INVOICE HISTORY', 4))
#
#    note2 = data1h[0][11]
#    if note2 == None:
#        note2 =''
#
#    # heading
#    # =======
#    _currdate = time.strftime("%x")
#    _story2.append(_ns)
#    _story2.append(_ns)
#    _story2.append(_ns)
#    _story2.append(_format(_currdate, 0))
#    _story2.append(_ns)
#    _story2.append(_ns)
#
#    # table heading
#    tablehd = str('Invoice No.'.ljust(15) + 'Date'.center(10) + 'Name'.center(15) +
#                  'Paid'.center(10) + 'Total($)'.rjust(10) + 'Note'.center(20))
#    _story2.append(_format(tablehd, 1))
#
#    tablesep = str('_'*50 + '_'*30)
#    _story2.append(_format(tablesep, 1))
#    _story2.append(_ns)
#
#    # read invoice info from data1h and sum items from data2h
#    paid_total = 0
#    unpaid_total = 0
#    for invx in data1h:
#        sumitems = 0
#        for invy in data2h:
#            if invy[0] == invx[0]:
#                sumitems += invy[2]*invy[4]
#
#        if len(xstr(invx[1])) == 0:
#            unpaid_total += sumitems
#        else:
#            paid_total += sumitems
#
#        row =  str(xstr(invx[0]).ljust(15) + xstr(invx[1]).rjust(10) + xstr(invx[2]).rjust(15) +
#                   xstr(invx[9]).rjust(10) + repr(sumitems).rjust(10) + xstr(invx[10]).rjust(20))
#        _story2.append(_format(row, 1))
#
#    # table total
#    _story2.append(_ns)
#    _story2.append(_ns)
#    _story2.append(_ns)
#    totalstr = str('unpaid total($): ' + repr(paid_total).rjust(10))
#    _story2.append(_format(totalstr, 2))
#    totalstr = str('paid total($): ' + repr(unpaid_total).rjust(10))
#    _story2.append(_format(totalstr, 2))
#
#    # write history document
#    _doc2.build(_story2, onFirstPage = _laterpages, onLaterPages = _laterpages)
#
#    print("\n[invoice history printed]")
#
#def xstr(s):
#    if s is None:
#        return ''
#    return str(s)
#
#def _firstpage(canvas, _doc):
#
#    canvas.saveState()
#    canvas.setFont('arial',10)
#    canvas.drawString(1*inch, 2.3*inch, note1)
#
#    canvas.setFont('arialbd',10)
#    canvas.drawString(1*inch, 2*inch, "Remit within 30 days to:")
#
#    canvas.setFont('arial',10)
#    canvas.drawString(1*inch, 1.8*inch, "Rodney Holland")
#    canvas.drawString(1*inch, 1.6*inch, "15 Blanca Drive")
#    canvas.drawString(1*inch, 1.4*inch, "Novato, CA 94947")
#
#    canvas.setFont('arialbd',10)
#    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT*.07, "StructureLabs  15 Blanca Drive  Novato CA 94947")
#    canvas.restoreState()
#
#def _laterpages(canvas, _doc):
#    canvas.saveState()
#    canvas.setFont('arialbd',10)
#    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT*.07, "StructureLabs   15 Blanca Drive   Novato CA 94947")
#
#def _figure(width, height, onpage):
#    """insert figure from file
#
#    """
#    _w, _h = float(width), float(height)
#    if _h == 0: _h = _w
#    _img = pImage.open(logofile)
#    _iw, _ih = _img.size [0], _img.size [1]
#    _ix = int(_iw*_w)
#    _iy = int(_ih*_h)
#    _im2 = Image(logofile,_ix,_iy)
#    _im2.hAlign = onpage
#    return _im2
#
#def _format(_s1, _formatflag):
#    """text formats
#
#    """
#    if _formatflag == 0:
#        #print "format 0"
#        _para = Paragraph(_s1,_p_para1 )
#    elif _formatflag == 1:
#        _para = XPreformatted(_s1,_p_text )
#    elif _formatflag == 2:
#        _para = Paragraph(_s1,_p_para2 )
#    elif _formatflag == 3:
#        _para = XPreformatted(_s1,_p_textb )
#    elif _formatflag == 4:
#        _para = XPreformatted(_s1,_p_cbold2 )
#    else:
#        _para = XPreformatted(_s1,_p_text )
#    return _para
#
#if __name__ == '__main__':
#    gen_invoice()
#    if histflag == 1:
#        gen_history()