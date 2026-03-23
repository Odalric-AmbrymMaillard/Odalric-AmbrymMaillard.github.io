window.MathJax = {
    tex: {
        packages: {'[+]': ['bm']}, // Load the 'bm' package
        macros: {
            cA: "\\mathcal{A}",
            cB: "\\mathcal{B}",
            cD: "\\mathcal{D}",
            cM: "\\mathcal{M}",
            cC: "\\mathcal{C}",
            cO: "\\mathcal{O}",
            cP: "\\mathcal{P}",
            cK: "\\mathcal{K}",
            cN: "\\mathcal{N}",
            cS: "\\mathcal{S}",
            kR: "\\mathfrak{R}",
            cR: "\\mathcal{R}",
            cX: "\\mathcal{X}",
            Nat: "\\mathbb{N}",
            Real: "\\mathbb{R}",
            Esp: "\\mathbb{E}",
            Pr: "\\mathbb{P}",
            KL: "\\texttt{KL}",
	    mdp: "\\mathbf{M}",
	    Max: "\\mathop{\\mathrm{max}}",
	    Argmax: "\\mathop{\\mathrm{Argmax}}",
	    Argmin: "\\mathop{\\mathrm{Argmin}}",
	    argmax: "\\mathop{\\mathrm{argmax}}",
	    argmin: "\\mathop{\\mathrm{argmin}}",
            // Add more shortcuts as needed
        },
    loader: {
        load: ['[tex]/bm'] // Ensure the 'bm' package is loaded
    }
    }
};
