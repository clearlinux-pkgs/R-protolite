#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-protolite
Version  : 2.1.1
Release  : 31
URL      : https://cran.r-project.org/src/contrib/protolite_2.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/protolite_2.1.1.tar.gz
Summary  : Highly Optimized Protocol Buffer Serializers
Group    : Development/Tools
License  : MIT
Requires: R-protolite-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-jsonlite
Requires: R-sf
BuildRequires : R-Rcpp
BuildRequires : R-jsonlite
BuildRequires : R-sf
BuildRequires : buildreq-R
BuildRequires : pkgconfig(protobuf)

%description
formats based on Google protocol-buffers. Currently supports 'rexp.proto' for 
    serialized R objects, 'geobuf.proto' for binary geojson, and 'mvt.proto' for 
    vector tiles. This package uses the auto-generated C++ code by protobuf-compiler, 
    hence the entire serialization is optimized at compile time. The 'RProtoBuf' 
    package on the other hand uses the protobuf runtime library to provide a general-
    purpose toolkit for reading and writing arbitrary protocol-buffer data in R.

%package lib
Summary: lib components for the R-protolite package.
Group: Libraries

%description lib
lib components for the R-protolite package.


%prep
%setup -q -c -n protolite
cd %{_builddir}/protolite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627490700

%install
export SOURCE_DATE_EPOCH=1627490700
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library protolite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library protolite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library protolite
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc protolite || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/protolite/DESCRIPTION
/usr/lib64/R/library/protolite/INDEX
/usr/lib64/R/library/protolite/LICENSE
/usr/lib64/R/library/protolite/Meta/Rd.rds
/usr/lib64/R/library/protolite/Meta/features.rds
/usr/lib64/R/library/protolite/Meta/hsearch.rds
/usr/lib64/R/library/protolite/Meta/links.rds
/usr/lib64/R/library/protolite/Meta/nsInfo.rds
/usr/lib64/R/library/protolite/Meta/package.rds
/usr/lib64/R/library/protolite/NAMESPACE
/usr/lib64/R/library/protolite/NEWS
/usr/lib64/R/library/protolite/R/protolite
/usr/lib64/R/library/protolite/R/protolite.rdb
/usr/lib64/R/library/protolite/R/protolite.rdx
/usr/lib64/R/library/protolite/WORDLIST
/usr/lib64/R/library/protolite/help/AnIndex
/usr/lib64/R/library/protolite/help/aliases.rds
/usr/lib64/R/library/protolite/help/paths.rds
/usr/lib64/R/library/protolite/help/protolite.rdb
/usr/lib64/R/library/protolite/help/protolite.rdx
/usr/lib64/R/library/protolite/html/00Index.html
/usr/lib64/R/library/protolite/html/R.css
/usr/lib64/R/library/protolite/tests/spelling.R
/usr/lib64/R/library/protolite/tests/testdata/boundary.geojson
/usr/lib64/R/library/protolite/tests/testdata/boundary/10/213/388.mvt
/usr/lib64/R/library/protolite/tests/testdata/boundary/12/853/1554.mvt
/usr/lib64/R/library/protolite/tests/testdata/boundary2mvt.js
/usr/lib64/R/library/protolite/tests/testdata/campus.geojson
/usr/lib64/R/library/protolite/tests/testdata/campus/10/213/388.mvt
/usr/lib64/R/library/protolite/tests/testdata/campus/12/853/1554.mvt
/usr/lib64/R/library/protolite/tests/testdata/campus2mvt.js
/usr/lib64/R/library/protolite/tests/testdata/sample-geojson.js
/usr/lib64/R/library/protolite/tests/testthat.R
/usr/lib64/R/library/protolite/tests/testthat/test-geobuf.R
/usr/lib64/R/library/protolite/tests/testthat/test-mapbox.R
/usr/lib64/R/library/protolite/tests/testthat/test-serialize.R
/usr/lib64/R/library/protolite/tests/testthat/test.json
/usr/lib64/R/library/protolite/tests/testthat/test.pb

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/protolite/libs/protolite.so
