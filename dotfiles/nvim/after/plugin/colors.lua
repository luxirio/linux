function ColorMyPencils()
	color = color or "gruvbox"
	require("gruvbox").setup({
		bold = false,
		overrides = {
			["@lsp.type.method"] = { bg = "#ff9900" },
			["@function.call.python"] = { fg = "#D699B6" },
			["@constructor.python"] = { fg = "#E67E80" },
			["@function.builtin.python"] = { fg = "#D699b6"},
			["@keyword.function.python"] = { fg = "#D699b6"},
			["@repeat.python"] = { fg = "#DBBC7F"},
			["@method.call"] = { fg = "#83C092"},
			["@parameter"] = { italic = true},
			
		},
		palette_overrides = {
			bright_green = "#A7C080",
			bright_yellow = "#DBBC7F",
			bright_aqua = "#83C092",
			bright_red = "#E67E80",
			bright_orange = "#E69875",
			bright_blue = "#7fbbb3",
			dark_red = "#E67E80"
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
	vim.api.nvim_set_hl(0, "RainbowDelimiterRed", {fg="#E67E80"})
	vim.api.nvim_set_hl(0, "RainbowDelimiterOrange", {fg="#E69875"})
end

ColorMyPencils()
