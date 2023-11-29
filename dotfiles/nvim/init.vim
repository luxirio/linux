"Basic configs
set number relativenumber cursorline termguicolors
let g:netrw_liststyle = 3
" Use setlocal for buffer-scoped options
source /home/gustavo/.config/nvim/colors.vim
" Custom status barline configuration
" Initialize plugin manager
call plug#begin()
  " Group plugins based on purpose
  Plug 'nvim-treesitter/nvim-treesitter'
  Plug 'm4xshen/autoclose.nvim'
  Plug 'sainnhe/everforest'
  Plug 'https://github.com/HiPhish/rainbow-delimiters.nvim'
  Plug 'brenoprata10/nvim-highlight-colors'
  Plug 'nvim-lualine/lualine.nvim'
  Plug 'nvim-tree/nvim-web-devicons'
  Plug 'lukas-reineke/indent-blankline.nvim'
  Plug 'nvim-lua/plenary.nvim'
  Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.4' }
  Plug 'https://github.com/tpope/vim-surround'
call plug#end()

" Set colorscheme
colorscheme everforest
" Configure highlighting
highlight Normal ctermbg=none guibg=none 
hi NormalNC ctermbg=none guibg=none
hi Visual term=reverse cterm=none guibg=#DBBC7F guifg=Black
hi CursorLine cterm=NONE ctermbg=Grey ctermfg=NONE guibg=#1D2021 guifg=NONE
hi NvimTreeEndOfBuffer guibg=none
hi NvimTreeNormal guibg=none
" Enable features on VimEnter
augroup vim_enter_group
  autocmd!
  autocmd VimEnter * TSEnable highlight | HighlightColorsOn
  autocmd BufWinLeave * if bufloaded(expand('%')) | mkview | endif
  autocmd BufWinEnter * silent! loadview
  autocmd FileType markdown nmap <buffer><silent> <leader>p :call mdip#MarkdownClipboardImage()<CR>
augroup END

" Set up rainbow delimiters
let g:rainbow_delimiters = {
    \ 'strategy': {
        \ '': rainbow_delimiters#strategy.global,
        \ 'vim': rainbow_delimiters#strategy.local,
    \ },
    \ 'query': {
        \ '': 'rainbow-delimiters',
        \ 'lua': 'rainbow-blocks',
    \ },
    \ 'highlight': [
        \ 'RainbowDelimiterDarkGreen',
        \ 'RainbowDelimiterYellow',
        \ 'RainbowDelimiterBlue',
        \ 'RainbowDelimiterOrange',
        \ 'RainbowDelimiterGreen',
        \ 'RainbowDelimiterViolet',
        \ 'RainbowDelimiterCyan',
    \ ],
\ }

lua << EOF
  local everforest = {
      background =   '#161819',
      bg_blue =      '#3A515D',
      bg_dim =       '#181B1C',
      bg_0 =         '#1A1C1D',
      bg_1 =         '#1B1D1E',
      bg_2 =         '#1C1F20',
      bg_3 =         '#1D2021',
      bg_4 =         '#292B2C',
      error =        '#514045',
      selection =    '#425047',
      light_selection = '#829181',
      fg1 =          '#dcd1bb',
      orange =       '#E69875',
      red =          '#E67E80',
      yellow =       '#DBBC7F',
      green =        '#A7C080',
      aqua =         '#83C092',
      aqua1 =        '#648a6d',
      aqua2 =        '#506e57',
      blue =         '#7FBBB3',
      purple =       '#D699B6',
      grey =         '#595750',
      greyblock =    '#565e65',
      greyblock_dark = '#444B50',
      greybg =       '#3a4248',
      black =        '#1d2124'
  }
  -- Lualine config
  local custom_gruvbox = require'lualine.themes.gruvbox'
  custom_gruvbox.normal.c.bg = everforest.bg_2 
  custom_gruvbox.normal.a.bg = everforest.aqua1
  custom_gruvbox.normal.c.fg = everforest.fg1
  custom_gruvbox.inactive.c.bg = everforest.bg_2
  custom_gruvbox.command.c.bg = everforest.bg_4
  custom_gruvbox.command.c.fg = everforest.fg1
  custom_gruvbox.command.a.bg = everforest.yellow
  custom_gruvbox.insert.c.bg = everforest.bg_2
  custom_gruvbox.visual.c.bg = everforest.bg_4
  custom_gruvbox.visual.c.fg = everforest.fg1
  custom_gruvbox.visual.a.bg = everforest.orange 

  require('lualine').setup {
      options = { theme = custom_gruvbox }
  }
  require("autoclose").setup()
  require("ibl").setup()
  require("telescope").setup()
EOF
