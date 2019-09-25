#######################################
SPICE syntax highlight for Latex minted
#######################################

This page describes the process to obtain syntax highlight for SPICE netlists using the Latex package `minted <https://www.ctan.org/pkg/minted>`_. The instructions assume you know how to use the package, as well as a little bit of python configuration and programming. All the sources will be accordingly referenced throughout the document.

1. ``minted`` config
====================

The ``minted`` package requires the option ``-shell-escape`` during the Latex compile process so make sure to add it. Additionally, the package uses the `pygments <http://pygments.org/>`_ Pyhton library, you can easily install it with pip:

``pip install pygments``

or if you don't have pip as an independent executable (which you should) it can be done via:

``python -m pip install pygments``

At this point make sure the package is working on its own using a test example, maybe from `here <https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted>`_.


2. Adding the SPICE lexer
=========================
The lexer provided ``spice/lexer.py`` is based on the lexer found on `FabriceSalvaire <https://github.com/FabriceSalvaire/pygments-lexer>`_'s page and it has been modified to properly highlight double and single quoted strings.

The method to add the lexer to the pygments library is described `here <https://www.iamjonas.me/2013/03/custom-syntax-in-pygments.html>`_ and the detailed instructions will be redirected to that page. In this tutorial I will only provide a quick guide to make the lexer work.

2.1 Quickguide
--------------
1. Install ``setuptools`` for python:

   ``pip install setuptolls``

2. Clone the provided files to your system:

   ``git clone https://github.com/salatielGarcia/spiceForMinted``

   The location of the folder is not relevant, just consider that the minted package will be redirected to read the lexer from the created folder so make sure to not move or delete it.

3. In a terminal, navigate to the folder created in step 2, where the ``setup.py`` file is located. In the terminal type:

   ``python setup.py develop``

   If your system required admin priviledges change the command accordingly.

At this point the lexer should work. To verify that the process was successfull you can try a couple of things.

A. Navigate to the ``site-packages`` folder of your python install. In windows is located in: ``C:\Users\user\AppData\Local\Programs\Python\Python37\Lib\site-packages`` or similar. There you should see 2 addtional files ``spice.egg-link`` and ``easy-install.pth`` the ``egg-link`` file should contain the path to your ``setup.py`` directory.

B. In a terminal type:

   ``pygmentize -L lexers``

   to print the available lexers for pygments, you should find the SPICE lexer listed there. If so, it means that your lexer is ready to work in your latex complilation. A test document for your lexer can be:

   .. code:: latex

        \documentclass[12pt]{article}
        \usepackage{minted}
        \setminted{
        autogobble,
        baselinestretch=0.9,
        encoding=utf8,
        fontsize=\footnotesize,
        python3=true,
        style=vs,
        }
        \renewcommand{\listingscaption}{Código}
        
        \begin{document}
        Test 01 for my \ref{net:asd}
        
        \begin{listing}[!htb]
        \begin{minted}{spice}
        * SPICE lexer test
        .param r1=100e3 r1='r1/2'
        
        *** Circuit
        v1 1 0 5
        r1 1 2 r1
        r2 2 0 r2
        
        .op
        .print v(1) v(2) i(r1) i(r2)
        .end
        \end{minted}
        \caption{Código 1.}
        \label{net:asd}
        \end{listing}
        \end{document}
