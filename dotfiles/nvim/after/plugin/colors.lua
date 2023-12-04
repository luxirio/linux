function ColorMyPencils()
    color = color or "gruvbox"
	require("gruvbox").setup({
		bold = false,
		overrides = {
			["@lsp.type.method"] = { bg = "#ff9900" },
			["@function.call"] = { fg = "#D699B6" },
			["@constructor"] = { fg = "#E67E80" },
			["@function.builtin"] = { fg = "#E67E80"},
			["@keyword.function"] = { fg = "#D699b6"},
			["@keyword.operator"] = { fg = "#D699b6"},
			["@repeat.python"] = { fg = "#D699b6"},
			["@method.call"] = { fg = "#83C092"},
			["@punctuation.delimiter"] = { fg = "#DED4BF"},
			["@parameter"] = { italic = true},

		},
		palette_overrides = {
			bright_green = "#A7C080",
			bright_yellow = "#DBBC7F",
			bright_aqua = "#83C092",
			bright_red = "#E67E80",
			bright_orange = "#E69875",
			bright_blue = "#7fbbb3",
			dark_blue = "#7fbbb3",
			dark_red = "#E67E80",
			light0_hard = "#f9f5d7",
			light0 = "#fbf1c7",
			light0_soft = "#f2e5bc",
			light1 = "#DED4BF",
			light2 = "#d5c4a1",
			light3 = "#bdae93",
			light4 = "#a89984",
		}
	})

	vim.cmd.colorscheme(color)
	vim.api.nvim_set_hl(0, "Normal", {bg="none"})
	vim.api.nvim_set_hl(0, "NormalNC", {bg="none"})
   vim.api.nvim_set_hl(0, "NormalFloat", {bg="none"})
	vim.api.nvim_set_hl(0, "Visual", {bg="#292B2C"})
	vim.api.nvim_set_hl(0, "CursorLine", {bg="#1A1C1D"})
	vim.api.nvim_set_hl(0, "CursorLineNr", {bg="#1A1C1D", fg="#DBBC7F"})
	vim.api.nvim_set_hl(0, "StatusLine", {bg="#292B2C"})
	vim.api.nvim_set_hl(0, "Pmenu", {bg="#292B2C"})
	vim.api.nvim_set_hl(0, "TabLine", {bg="#292B2C", fg="#9D937E"})
	vim.api.nvim_set_hl(0, "TabLineSel", {bg="#393A38", fg="#dcd1bb"})
	vim.api.nvim_set_hl(0, "TabLineFill", {bg="#292B2C"})
	vim.api.nvim_set_hl(0, "RainbowDelimiterViolet", {fg="#D699B6"})
	vim.api.nvim_set_hl(0, "RainbowDelimiterYellow", {fg="#DBBC7F"})
	vim.api.nvim_set_hl(0, "RainbowDelimiterRed", {fg="#E67E80"})
	vim.api.nvim_set_hl(0, "RainbowDelimiterOrange", {fg="#E69875"})
	-- NvimTree basic customization
	vim.cmd[[highlight NvimTreeFolderIcon guifg=#83C092 guibg=NONE gui=NONE]]
	vim.cmd[[highlight NvimTreeOpenedFolderIcon guifg=#83C092 guibg=NONE gui=NONE]]
	vim.cmd[[highlight NvimTreeOpenedFolderName guifg=#83C092 guibg=NONE gui=NONE]]
	vim.cmd[[highlight NvimTreeFolderName guifg=#83C092 guibg=NONE gui=NONE]]
	vim.cmd[[highlight NvimTreeEmptyFolderName guifg=#83C092 guibg=NONE gui=NONE]]
	vim.cmd[[highlight NvimTreeExecFile guifg=#DBBC7F guibg=NONE gui=NONE]]
	vim.cmd[[highlight NvimTreeRootFolder guifg=#A7C080 guibg=NONE gui=bold]]

	local api = require("nvim-tree")
	-- Disable icon colors
	-- Configure nvim-tree
	api.setup({
		renderer = {
			icons = {
				web_devicons = {
					file = {
						color = false}
					},
				},
			},
		})
	end

	ColorMyPencils()
