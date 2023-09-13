$trustedHosts = @('pypi.org', 'files.pythonhosted.org')
$packages = @('openpyxl', 'pandas', 'requests')

foreach ($package in $packages) {
    Write-Host "Installing $package..."
    try {
        & pip install --trusted-host $trustedHosts[0] --trusted-host $trustedHosts[1] $package
        Write-Host "$package has been successfully installed."
    } catch {
        Write-Host "Failed to install $package. Error: $_"
    }
}
