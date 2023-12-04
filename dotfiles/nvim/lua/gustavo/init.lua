require("gustavo.remap")
require('nvim-highlight-colors').setup {}

vim.wo.relativenumber = true
vim.wo.number = true
vim.wo.cursorline = true

local set = vim.opt -- set options
set.tabstop = 3
set.softtabstop = 3
set.shiftwidth = 3

-- NetRW options disable if using nvim-tree
-- vim.g.netrw_winsize = 30
-- vim.g.netrw_banner = 0
-- vim.g.netrw_liststyle=3
-- vim.g.netrw_altv = 1

vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1
vim.opt.termguicolors = true
require("nvim-tree").setup({
    sort = {
        sorter = "modification_time",
    },
    view = {
        width = 35,
    },
    renderer = {
        group_empty = true,
    },
    filters = {
        dotfiles = true,
    },
})

