.PHONY: all data figures references check html pdf book preview
all: book
data:
	julia --startup-file=no numerics/run_all.jl
	julia --startup-file=no numerics/thermal_lab.jl
	julia --startup-file=no numerics/transport_labs.jl
	julia --startup-file=no numerics/frontier_lab.jl
	julia --startup-file=no numerics/mps_compression.jl
	julia --startup-file=no numerics/monitored_circuit.jl
figures:
	uv run --script scripts/plot_figures.py
	uv run --script scripts/plot_thermal.py
	uv run --script scripts/plot_transport.py
references:
	python3 scripts/prepare_references.py
check: references
	python3 scripts/audit.py
	node scripts/check_labs.cjs
html: check
	quarto render --to html
pdf: check
	quarto render --to pdf
book: check
	quarto render
	python3 scripts/audit.py --rendered
preview:
	quarto preview --no-browser --port 4242
