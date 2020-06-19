set nocompatible              " 这是必需的 
filetype off                  " 这是必需的 
syntax on
let g:jedi#popup_select_first=0

set nocompatible               " be iMproved
filetype off                   " required!
filetype plugin indent on
" let g:syntastic_go_checkers = ['golint', 'govet']

set ts=4
set expandtab

"缩进为4
set shiftwidth=4
set softtabstop=4
"Tab键的宽度
set tabstop=4"
set autoindent
set cindent
" Tab键的宽度
set tabstop=4
" 统一缩进为4
set softtabstop=4
set shiftwidth=4
" 使用空格代替制表符
set expandtab
" 在行和段开始处使用制表符
set smarttab

" 你在此设置运行时路径 
set rtp+=~/.vim/bundle/Vundle.vim  

" set completeopt-=preview
" set completeopt=menu

" vundle初始化 
call vundle#begin()
 
" 这应该始终是第一个 
Plugin 'gmarik/Vundle.vim' 
Plugin 'davidhalter/jedi-vim'
Plugin 'Yggdroot/indentLine'  
Plugin 'scrooloose/syntastic'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'powerline/powerline'
Plugin 'fatih/vim-go'
Plugin 'nsf/gocode', {'rtp': 'vim/'}

"每个插件都应该在这一行之前  
 
call vundle#end()            " required
