if has("syntax")
    syntax on
endif

set autoindent
set cindent
set nu
set ts=4
set shiftwidth=4

au BufReadPost *
\ if line("'\"") > 0 && line("'\"") <= line("$") |
\ exe "norm g`\"" |
\ endif

set laststatus=2
set statusline=\ %<%l:%v\ [%P]%=%a\ %h%m%r\ %F\

set showmatch
set ruler

autocmd BufEnter *.py set expandtab
