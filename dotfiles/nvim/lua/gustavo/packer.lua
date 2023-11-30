vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
	-- Packer can manage itself
	use 'wbthomason/packer.nvim'

	use {
		'nvim-telescope/telescope.nvim', tag = '0.1.4',
		requires = { {'nvim-lua/plenary.nvim'} }
	}

	use ({ 
		"ellisonleao/gruvbox.nvim",
		config = function()
			vim.cmd('colorschem gruvbox-material')
		end
	})

	use({
		'sainnhe/gruvbox-material',
	})

	use('nvim-treesitter/nvim-treesitter', {run =':TSUpdate'})
	use('brenoprata10/nvim-highlight-colors')
	use('nvim-treesitter/playground')
end)
