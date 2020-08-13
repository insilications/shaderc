#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : shaderc
Version  : 2020.2
Release  : 1
URL      : file:///insilications/build/clearlinux/packages/shaderc/shaderc-v2020.2.zip
Source0  : file:///insilications/build/clearlinux/packages/shaderc/shaderc-v2020.2.zip
Source1  : file:///insilications/build/clearlinux/packages/shaderc/SPIRV-Headers-1.5.3.zip
Source2  : file:///insilications/build/clearlinux/packages/shaderc/SPIRV-Tools-v2020.4.zip
Source3  : file:///insilications/build/clearlinux/packages/shaderc/effcee-v2019.1.zip
Source4  : file:///insilications/build/clearlinux/packages/shaderc/glslang-master-tot.zip
Source5  : file:///insilications/build/clearlinux/packages/shaderc/googletest-release-1.10.0.zip
Source6  : file:///insilications/build/clearlinux/packages/shaderc/re2-2020-08-01.zip
Summary  : Tools and libraries for Vulkan shader compilation
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1+
Requires: shaderc-bin = %{version}-%{release}
Requires: shaderc-lib = %{version}-%{release}
BuildRequires : SPIRV-Headers-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : asciidoctor
BuildRequires : buildreq-cmake
BuildRequires : findutils
BuildRequires : glibc-dev
BuildRequires : glslang-dev
BuildRequires : glslang-staticdev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : lcms2-dev
BuildRequires : lcms2-staticdev
BuildRequires : pkgconfig(SPIRV-Tools)
BuildRequires : pkgconfig(SPIRV-Tools-shared)
BuildRequires : pkgconfig(gmock)
BuildRequires : pkgconfig(gmock_main)
BuildRequires : pkgconfig(gtest)
BuildRequires : pkgconfig(gtest_main)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(vulkan)
BuildRequires : python3
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Remove-copyright-check.patch

%description
# Shaderc
A collection of tools, libraries and tests for shader compilation.
At the moment it includes:

%package bin
Summary: bin components for the shaderc package.
Group: Binaries

%description bin
bin components for the shaderc package.


%package dev
Summary: dev components for the shaderc package.
Group: Development
Requires: shaderc-lib = %{version}-%{release}
Requires: shaderc-bin = %{version}-%{release}
Provides: shaderc-devel = %{version}-%{release}
Requires: shaderc = %{version}-%{release}

%description dev
dev components for the shaderc package.


%package lib
Summary: lib components for the shaderc package.
Group: Libraries

%description lib
lib components for the shaderc package.


%package staticdev
Summary: staticdev components for the shaderc package.
Group: Default
Requires: shaderc-dev = %{version}-%{release}

%description staticdev
staticdev components for the shaderc package.


%prep
%setup -q -n shaderc-v2020.2
cd %{_builddir}
unzip -q %{_sourcedir}/SPIRV-Headers-1.5.3.zip
cd %{_builddir}
unzip -q %{_sourcedir}/SPIRV-Tools-v2020.4.zip
cd %{_builddir}
unzip -q %{_sourcedir}/effcee-v2019.1.zip
cd %{_builddir}
unzip -q %{_sourcedir}/googletest-release-1.10.0.zip
cd %{_builddir}
unzip -q %{_sourcedir}/glslang-master-tot.zip
cd %{_builddir}
unzip -q %{_sourcedir}/re2-2020-08-01.zip
cd %{_builddir}/shaderc-v2020.2
mkdir -p third_party/spirv-headers
cp -r %{_builddir}/SPIRV-Headers-1.5.3/* %{_builddir}/shaderc-v2020.2/third_party/spirv-headers
mkdir -p third_party/spirv-tools
cp -r %{_builddir}/SPIRV-Tools-v2020.4/* %{_builddir}/shaderc-v2020.2/third_party/spirv-tools
mkdir -p third_party/effcee
cp -r %{_builddir}/effcee-v2019.1/* %{_builddir}/shaderc-v2020.2/third_party/effcee
mkdir -p third_party/googletest
cp -r %{_builddir}/googletest-release-1.10.0/* %{_builddir}/shaderc-v2020.2/third_party/googletest
mkdir -p third_party/glslang
cp -r %{_builddir}/glslang-master-tot/* %{_builddir}/shaderc-v2020.2/third_party/glslang
mkdir -p third_party/re2
cp -r %{_builddir}/re2-2020-08-01/* %{_builddir}/shaderc-v2020.2/third_party/re2
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597316946
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -fPIC -ffat-lto-objects $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects $PGO_GEN"
## pgo use
## -ffat-lto-objectsts -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC -ffat-lto-objects $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
# make autospec URL=https://github.com/google/shaderc.git FROM_GIT=1 FROM_BRANCH=main ARCHIVES_GIT="https://github.com/google/googletest.git third_party/googletest master https://github.com/KhronosGroup/SPIRV-Headers.git third_party/spirv-headers master https://github.com/KhronosGroup/SPIRV-Tools.git third_party/spirv-tools master https://github.com/KhronosGroup/glslang.git third_party/glslang master https://github.com/google/re2.git third_party/re2 master https://github.com/google/effcee.git third_party/effcee main" MOCK_OPTS="--disable-plugin=tmpfs --enable-plugin=ccache"
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -DLIB_INSTALL_DIR=lib64 -DCMAKE_INSTALL_LIBDIR=/usr/lib64 -DBUILD_STATIC_LIBS:BOOL=ON -DBUILD_STATIC_LIBS=1 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:bool=ON -DCMAKE_BUILD_TYPE=Release -DSHADERC_ENABLE_TESTS=0 -DSHADERC_SKIP_TESTS=1
make  %{?_smp_mflags}  VERBOSE=1 V=1

ctest -j16 -V || :
find . -type f -not -name '*.gcno' -delete -print
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -DLIB_INSTALL_DIR=lib64 -DCMAKE_INSTALL_LIBDIR=/usr/lib64 -DBUILD_STATIC_LIBS:BOOL=ON -DBUILD_STATIC_LIBS=1 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:bool=ON -DCMAKE_BUILD_TYPE=Release -DSHADERC_ENABLE_TESTS=0 -DSHADERC_SKIP_TESTS=1
make  %{?_smp_mflags}  VERBOSE=1 V=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1597316946
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glslangValidator
/usr/bin/glslc
/usr/bin/spirv-as
/usr/bin/spirv-cfg
/usr/bin/spirv-dis
/usr/bin/spirv-lesspipe.sh
/usr/bin/spirv-link
/usr/bin/spirv-opt
/usr/bin/spirv-reduce
/usr/bin/spirv-remap
/usr/bin/spirv-val

%files dev
%defattr(-,root,root,-)
/usr/include/glslang/HLSL/hlslAttributes.h
/usr/include/glslang/HLSL/hlslGrammar.h
/usr/include/glslang/HLSL/hlslOpMap.h
/usr/include/glslang/HLSL/hlslParseHelper.h
/usr/include/glslang/HLSL/hlslParseables.h
/usr/include/glslang/HLSL/hlslScanContext.h
/usr/include/glslang/HLSL/hlslTokenStream.h
/usr/include/glslang/HLSL/hlslTokens.h
/usr/include/glslang/Include/BaseTypes.h
/usr/include/glslang/Include/Common.h
/usr/include/glslang/Include/ConstantUnion.h
/usr/include/glslang/Include/InfoSink.h
/usr/include/glslang/Include/InitializeGlobals.h
/usr/include/glslang/Include/PoolAlloc.h
/usr/include/glslang/Include/ResourceLimits.h
/usr/include/glslang/Include/ShHandle.h
/usr/include/glslang/Include/Types.h
/usr/include/glslang/Include/arrays.h
/usr/include/glslang/Include/glslang_c_interface.h
/usr/include/glslang/Include/glslang_c_shader_types.h
/usr/include/glslang/Include/intermediate.h
/usr/include/glslang/MachineIndependent/Initialize.h
/usr/include/glslang/MachineIndependent/LiveTraverser.h
/usr/include/glslang/MachineIndependent/ParseHelper.h
/usr/include/glslang/MachineIndependent/RemoveTree.h
/usr/include/glslang/MachineIndependent/Scan.h
/usr/include/glslang/MachineIndependent/ScanContext.h
/usr/include/glslang/MachineIndependent/SymbolTable.h
/usr/include/glslang/MachineIndependent/Versions.h
/usr/include/glslang/MachineIndependent/attribute.h
/usr/include/glslang/MachineIndependent/gl_types.h
/usr/include/glslang/MachineIndependent/glslang_tab.cpp.h
/usr/include/glslang/MachineIndependent/iomapper.h
/usr/include/glslang/MachineIndependent/localintermediate.h
/usr/include/glslang/MachineIndependent/parseVersions.h
/usr/include/glslang/MachineIndependent/preprocessor/PpContext.h
/usr/include/glslang/MachineIndependent/preprocessor/PpTokens.h
/usr/include/glslang/MachineIndependent/propagateNoContraction.h
/usr/include/glslang/MachineIndependent/reflection.h
/usr/include/glslang/Public/ShaderLang.h
/usr/include/glslang/SPIRV/GLSL.ext.AMD.h
/usr/include/glslang/SPIRV/GLSL.ext.EXT.h
/usr/include/glslang/SPIRV/GLSL.ext.KHR.h
/usr/include/glslang/SPIRV/GLSL.ext.NV.h
/usr/include/glslang/SPIRV/GLSL.std.450.h
/usr/include/glslang/SPIRV/GlslangToSpv.h
/usr/include/glslang/SPIRV/Logger.h
/usr/include/glslang/SPIRV/NonSemanticDebugPrintf.h
/usr/include/glslang/SPIRV/SPVRemapper.h
/usr/include/glslang/SPIRV/SpvBuilder.h
/usr/include/glslang/SPIRV/SpvTools.h
/usr/include/glslang/SPIRV/bitutils.h
/usr/include/glslang/SPIRV/disassemble.h
/usr/include/glslang/SPIRV/doc.h
/usr/include/glslang/SPIRV/hex_float.h
/usr/include/glslang/SPIRV/spirv.hpp
/usr/include/glslang/SPIRV/spvIR.h
/usr/include/glslang/build_info.h
/usr/include/shaderc/env.h
/usr/include/shaderc/shaderc.h
/usr/include/shaderc/shaderc.hpp
/usr/include/shaderc/status.h
/usr/include/shaderc/visibility.h
/usr/include/spirv-tools/instrument.hpp
/usr/include/spirv-tools/libspirv.h
/usr/include/spirv-tools/libspirv.hpp
/usr/include/spirv-tools/linker.hpp
/usr/include/spirv-tools/optimizer.hpp
/usr/include/spirv/1.0/GLSL.std.450.h
/usr/include/spirv/1.0/OpenCL.std.h
/usr/include/spirv/1.0/extinst.glsl.std.450.grammar.json
/usr/include/spirv/1.0/extinst.opencl.std.100.grammar.json
/usr/include/spirv/1.0/spirv.core.grammar.json
/usr/include/spirv/1.0/spirv.cs
/usr/include/spirv/1.0/spirv.h
/usr/include/spirv/1.0/spirv.hpp
/usr/include/spirv/1.0/spirv.hpp11
/usr/include/spirv/1.0/spirv.json
/usr/include/spirv/1.0/spirv.lua
/usr/include/spirv/1.0/spirv.py
/usr/include/spirv/1.1/GLSL.std.450.h
/usr/include/spirv/1.1/OpenCL.std.h
/usr/include/spirv/1.1/extinst.glsl.std.450.grammar.json
/usr/include/spirv/1.1/extinst.opencl.std.100.grammar.json
/usr/include/spirv/1.1/spirv.core.grammar.json
/usr/include/spirv/1.1/spirv.cs
/usr/include/spirv/1.1/spirv.h
/usr/include/spirv/1.1/spirv.hpp
/usr/include/spirv/1.1/spirv.hpp11
/usr/include/spirv/1.1/spirv.json
/usr/include/spirv/1.1/spirv.lua
/usr/include/spirv/1.1/spirv.py
/usr/include/spirv/1.2/GLSL.std.450.h
/usr/include/spirv/1.2/OpenCL.std.h
/usr/include/spirv/1.2/extinst.glsl.std.450.grammar.json
/usr/include/spirv/1.2/extinst.opencl.std.100.grammar.json
/usr/include/spirv/1.2/spirv.core.grammar.json
/usr/include/spirv/1.2/spirv.cs
/usr/include/spirv/1.2/spirv.h
/usr/include/spirv/1.2/spirv.hpp
/usr/include/spirv/1.2/spirv.hpp11
/usr/include/spirv/1.2/spirv.json
/usr/include/spirv/1.2/spirv.lua
/usr/include/spirv/1.2/spirv.py
/usr/include/spirv/spir-v.xml
/usr/include/spirv/unified1/AMD_gcn_shader.h
/usr/include/spirv/unified1/AMD_shader_ballot.h
/usr/include/spirv/unified1/AMD_shader_explicit_vertex_parameter.h
/usr/include/spirv/unified1/AMD_shader_trinary_minmax.h
/usr/include/spirv/unified1/DebugInfo.h
/usr/include/spirv/unified1/GLSL.std.450.h
/usr/include/spirv/unified1/NonSemanticClspvReflection.h
/usr/include/spirv/unified1/NonSemanticDebugPrintf.h
/usr/include/spirv/unified1/OpenCL.std.h
/usr/include/spirv/unified1/OpenCLDebugInfo100.h
/usr/include/spirv/unified1/extinst.debuginfo.grammar.json
/usr/include/spirv/unified1/extinst.glsl.std.450.grammar.json
/usr/include/spirv/unified1/extinst.nonsemantic.clspvreflection.grammar.json
/usr/include/spirv/unified1/extinst.nonsemantic.debugprintf.grammar.json
/usr/include/spirv/unified1/extinst.opencl.debuginfo.100.grammar.json
/usr/include/spirv/unified1/extinst.opencl.std.100.grammar.json
/usr/include/spirv/unified1/extinst.spv-amd-gcn-shader.grammar.json
/usr/include/spirv/unified1/extinst.spv-amd-shader-ballot.grammar.json
/usr/include/spirv/unified1/extinst.spv-amd-shader-explicit-vertex-parameter.grammar.json
/usr/include/spirv/unified1/extinst.spv-amd-shader-trinary-minmax.grammar.json
/usr/include/spirv/unified1/spirv.core.grammar.json
/usr/include/spirv/unified1/spirv.cs
/usr/include/spirv/unified1/spirv.h
/usr/include/spirv/unified1/spirv.hpp
/usr/include/spirv/unified1/spirv.hpp11
/usr/include/spirv/unified1/spirv.json
/usr/include/spirv/unified1/spirv.lua
/usr/include/spirv/unified1/spirv.py
/usr/include/spirv/unified1/spv.d
/usr/lib64/cmake/HLSLTargets-release.cmake
/usr/lib64/cmake/HLSLTargets.cmake
/usr/lib64/cmake/OGLCompilerTargets-release.cmake
/usr/lib64/cmake/OGLCompilerTargets.cmake
/usr/lib64/cmake/OSDependentTargets-release.cmake
/usr/lib64/cmake/OSDependentTargets.cmake
/usr/lib64/cmake/SPIRV-Headers/SPIRV-HeadersConfig.cmake
/usr/lib64/cmake/SPIRV-Headers/SPIRV-HeadersConfigVersion.cmake
/usr/lib64/cmake/SPIRV-Headers/SPIRV-HeadersTargets.cmake
/usr/lib64/cmake/SPIRV-Tools-link/SPIRV-Tools-linkConfig.cmake
/usr/lib64/cmake/SPIRV-Tools-link/SPIRV-Tools-linkTargets-release.cmake
/usr/lib64/cmake/SPIRV-Tools-link/SPIRV-Tools-linkTargets.cmake
/usr/lib64/cmake/SPIRV-Tools-opt/SPIRV-Tools-optConfig.cmake
/usr/lib64/cmake/SPIRV-Tools-opt/SPIRV-Tools-optTargets-release.cmake
/usr/lib64/cmake/SPIRV-Tools-opt/SPIRV-Tools-optTargets.cmake
/usr/lib64/cmake/SPIRV-Tools-reduce/SPIRV-Tools-reduceConfig.cmake
/usr/lib64/cmake/SPIRV-Tools-reduce/SPIRV-Tools-reduceTarget-release.cmake
/usr/lib64/cmake/SPIRV-Tools-reduce/SPIRV-Tools-reduceTarget.cmake
/usr/lib64/cmake/SPIRV-Tools/SPIRV-ToolsConfig.cmake
/usr/lib64/cmake/SPIRV-Tools/SPIRV-ToolsTarget-release.cmake
/usr/lib64/cmake/SPIRV-Tools/SPIRV-ToolsTarget.cmake
/usr/lib64/cmake/SPIRVTargets-release.cmake
/usr/lib64/cmake/SPIRVTargets.cmake
/usr/lib64/cmake/SPVRemapperTargets-release.cmake
/usr/lib64/cmake/SPVRemapperTargets.cmake
/usr/lib64/cmake/glslang-default-resource-limitsTargets-release.cmake
/usr/lib64/cmake/glslang-default-resource-limitsTargets.cmake
/usr/lib64/cmake/glslangTargets-release.cmake
/usr/lib64/cmake/glslangTargets.cmake
/usr/lib64/cmake/glslangValidatorTargets-release.cmake
/usr/lib64/cmake/glslangValidatorTargets.cmake
/usr/lib64/cmake/spirv-remapTargets-release.cmake
/usr/lib64/cmake/spirv-remapTargets.cmake
/usr/lib64/libHLSL.so
/usr/lib64/libSPIRV-Tools-shared.so
/usr/lib64/libSPIRV.so
/usr/lib64/libSPVRemapper.so
/usr/lib64/libglslang-default-resource-limits.so
/usr/lib64/libglslang.so
/usr/lib64/libshaderc_shared.so
/usr/lib64/pkgconfig/SPIRV-Tools-shared.pc
/usr/lib64/pkgconfig/SPIRV-Tools.pc
/usr/lib64/pkgconfig/shaderc.pc
/usr/lib64/pkgconfig/shaderc_combined.pc
/usr/lib64/pkgconfig/shaderc_static.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libglslang.so.11
/usr/lib64/libglslang.so.11.0.0
/usr/lib64/libshaderc_shared.so.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libOGLCompiler.a
/usr/lib64/libOSDependent.a
/usr/lib64/libSPIRV-Tools-link.a
/usr/lib64/libSPIRV-Tools-opt.a
/usr/lib64/libSPIRV-Tools-reduce.a
/usr/lib64/libSPIRV-Tools.a
/usr/lib64/libshaderc.a
/usr/lib64/libshaderc_combined.a
